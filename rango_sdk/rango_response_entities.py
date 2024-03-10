from dataclasses import dataclass, field
from typing import Optional, List, Dict, Union
from dataclasses_json import dataclass_json, config
from decimal import Decimal


@dataclass_json
@dataclass
class ExplorerUrl:
    url: str
    description: str


@dataclass_json
@dataclass
class BridgeExtra:
    requireRefundAction: bool
    srcTx: str
    destTx: str


@dataclass_json
@dataclass
class TransactionObject:
    status: str
    timestamp: int
    outputAmount: str
    explorerUrl: List[ExplorerUrl]
    bridgeExtra: BridgeExtra
    extraMessage: Optional[str] = None
    failedType: Optional[str] = None
    referrals: Optional[str] = None
    newTx: Optional[str] = None
    diagnosisUrl: Optional[str] = None
    steps: Optional[str] = None
    outputToken: Optional[str] = None

    def is_successful(self) -> bool:
        return self.status == "success"

    def get_output_amount(self) -> str:
        return '%.3f' % Decimal(self.outputAmount)

    def print_explorer_urls(self):
        msg = ''
        for ex in self.explorerUrl:
            msg += f'🔹 [Explorer Link]({ex.url}) -> {ex.description} \n'
            return msg


@dataclass_json
@dataclass
class Amount:
    amount: int
    decimals: int


@dataclass_json
@dataclass
class Asset:
    blockchain: str
    symbol: str
    address: Optional[str] = None
    name: Optional[str] = None
    decimals: Optional[int] = None

    def __repr__(self):
        return f'{self.blockchain}.{self.symbol}'


@dataclass_json
@dataclass
class SwapFee:
    asset: Asset
    expenseType: str
    amount: float
    name: str


@dataclass_json
@dataclass
class SwapNode:
    marketName: str
    percent: float
    marketId: Optional[str] = None


@dataclass_json
@dataclass
class SwapNode:
    nodes: List[SwapNode]


@dataclass_json
@dataclass
class SwapRoute:
    nodes: List[SwapNode]


@dataclass_json
@dataclass
class SwapResultAsset:
    symbol: str
    logo: str
    blockchainLogo: str
    blockchain: str
    decimals: int
    usdPrice: Optional[float] = None
    address: Optional[str] = None


@dataclass_json
@dataclass
class RecommendedSlippage:
    error: bool
    slippage: Optional[float] = None


@dataclass_json
@dataclass
class SwapResult:
    swapperId: str
    swapperType: str
    from_: SwapResultAsset = field(metadata=config(field_name='from'))
    to: SwapResultAsset
    fromAmount: float
    toAmount: float
    fee: List[SwapFee]
    estimatedTimeInSeconds: int
    swapChainType: str
    fromAsset: Optional[Asset] = None
    toAsset: Optional[Asset] = None
    swapperLogo: Optional[str] = None
    fromAmountPrecision: Optional[float] = None
    fromAmountMinValue: Optional[float] = None
    fromAmountMaxValue: Optional[float] = None
    fromAmountRestrictionType: Optional[str] = None
    routes: Optional[List[SwapRoute]] = None
    recommendedSlippage: Optional[RecommendedSlippage] = None
    warnings: Optional[List[str]] = None
    timeStat: Optional[Dict[str, int]] = None
    includesDestinationTx: Optional[bool] = None
    maxRequiredSign: Optional[int] = None
    isWrapped: Optional[bool] = None


@dataclass_json
@dataclass
class SimulationResult:
    outputAmount: float
    swaps: List[SwapResult]
    resultType: str


@dataclass_json
@dataclass
class BestRouteResponse:
    requestAmount: float
    requestId: str
    result: SimulationResult
    walletNotSupportingFromBlockchain: bool
    processingLimitReached: bool
    missingBlockchains: List[str]
    diagnosisMessages: List[str]
    compareStatus: str
    from_: Asset = field(metadata=config(field_name='from'))
    to: Asset


@dataclass_json
@dataclass
class Token:
    blockchain: str
    symbol: str
    isPopular: bool
    supportedSwappers: List[str]
    image: Optional[str] = None
    address: Optional[str] = None
    usdPrice: Optional[float] = None
    decimals: Optional[int] = None
    name: Optional[str] = None
    isSecondaryCoin: Optional[bool] = None
    coinSource: Optional[str] = None
    coinSourceUrl: Optional[str] = None


@dataclass_json
@dataclass
class BlockchainMeta:
    name: str
    defaultDecimals: int
    addressPatterns: List[str]
    feeAssets: List[Asset]
    logo: str
    displayName: str
    shortName: str
    sort: int
    color: str
    enabled: bool
    type: str
    chainId: Optional[str] = None
    info: Optional[dict] = None


@dataclass_json
@dataclass
class SwapperMetaDto:
    id: str
    title: str
    logo: str
    swapperGroup: str
    types: List[str]
    enabled: bool


@dataclass_json
@dataclass
class MetaResponse:
    tokens: List[Token]
    popularTokens: List[Token]
    blockchains: List[BlockchainMeta]
    swappers: List[SwapperMetaDto]


@dataclass_json
@dataclass
class GetWalletDetailsRequest:
    addresses: List[str]


@dataclass_json
@dataclass
class Balance:
    asset: Asset
    amount: Amount


@dataclass_json
@dataclass
class WalletDetails:
    address: str
    blockChain: str
    balances: List[Balance]


@dataclass_json
@dataclass
class BalanceResponse:
    wallets: List[WalletDetails]


# Create Transaction
@dataclass_json
@dataclass
class GenericTransaction:
    type: str


@dataclass_json
@dataclass
class CosmosTransaction(GenericTransaction):
    fromWalletAddress: str
    blockChain: str
    data: dict
    rawTransfer: Optional[dict] = None


@dataclass_json
@dataclass
class EvmTransaction(GenericTransaction):
    blockChain: str
    isApprovalTx: bool
    to: str
    data: Optional[str] = None
    value: Optional[str] = None
    gasLimit: Optional[str] = None
    gasPrice: Optional[int] = None
    maxPriorityFeePerGas: Optional[int] = None
    maxFeePerGas: Optional[int] = None
    nonce: Optional[int] = None
    from_: Optional[str] = field(default=None, metadata={"name": "from"})


@dataclass_json
@dataclass
class SolanaTransaction(GenericTransaction):
    blockChain: str
    from_: str = field(metadata={"name": "from"})
    identifier: str
    instructions: List[dict]
    signatures: List[dict]
    txType: str
    serializedMessage: Optional[str] = None
    recentBlockhash: Optional[str] = None


@dataclass_json
@dataclass
class StarkNetTransaction(GenericTransaction):
    blockChain: str
    calls: List[dict]
    isApprovalTx: bool
    maxFee: Optional[int] = None


@dataclass_json
@dataclass
class TransferTransaction(GenericTransaction):
    method: str
    fromWalletAddress: str
    recipientAddress: str
    amount: int
    decimals: int
    asset: Asset
    memo: Optional[str] = None


@dataclass_json
@dataclass
class TrxTransaction(GenericTransaction):
    blockChain: str
    isApprovalTx: bool
    txID: str
    visible: bool
    raw_data: Optional[dict] = None
    raw_data_hex: Optional[str] = None
    externalTxId: Optional[str] = None
    __payload__: Optional[dict] = None


@dataclass_json
@dataclass
class CreateTransactionResponse:
    ok: bool
    transaction: Union[
        CosmosTransaction, EvmTransaction, SolanaTransaction, StarkNetTransaction, TransferTransaction, TrxTransaction]
    error: Optional[str] = None
    errorCode: Optional[int] = None
