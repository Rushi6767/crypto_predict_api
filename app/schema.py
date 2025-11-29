from pydantic import BaseModel

class CryptoFeatures(BaseModel):
    total_vol: float
    price: float
    volume_24h: float
    change_7d: float
    marketcap: float
    price_to_mc: float
    vol_to_mc: float
    vol_to_price: float
    log_price: float
    log_vol: float
    log_marketcap: float
    abs_change_7d: float
    diff_change: float
    name_encodedr: int
    symbol_encoder: int
