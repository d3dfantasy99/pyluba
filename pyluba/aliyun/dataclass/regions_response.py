from dataclasses import dataclass
from typing import Optional, TypeVar

from mashumaro import DataClassDictMixin
from mashumaro.mixins.orjson import DataClassORJSONMixin

DataT = TypeVar("DataT")


@dataclass
class RegionResponseData(DataClassORJSONMixin):
    shortRegionId: str
    oaApiGatewayEndpoint: str
    regionId: str
    mqttEndpoint: str
    pushChannelEndpoint: str
    regionEnglishName: str
    apiGatewayEndpoint: str


@dataclass
class RegionResponse(DataClassDictMixin):
    data: RegionResponseData
    code: int
    id: Optional[str] = None
    msg: Optional[str] = None
