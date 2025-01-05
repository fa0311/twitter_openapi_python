# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from twitter_openapi_python_generated.models.type_name import TypeName
from twitter_openapi_python_generated.models.user_highlights_info import UserHighlightsInfo
from twitter_openapi_python_generated.models.user_legacy import UserLegacy
from twitter_openapi_python_generated.models.user_legacy_extended_profile import UserLegacyExtendedProfile
from twitter_openapi_python_generated.models.user_professional import UserProfessional
from twitter_openapi_python_generated.models.user_tip_jar_settings import UserTipJarSettings
from twitter_openapi_python_generated.models.user_verification_info import UserVerificationInfo
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    typename: TypeName = Field(alias="__typename")
    affiliates_highlighted_label: Optional[Dict[str, Any]] = None
    business_account: Optional[Dict[str, Any]] = None
    creator_subscriptions_count: Optional[StrictInt] = None
    has_graduated_access: Optional[StrictBool] = None
    has_hidden_likes_on_profile: Optional[StrictBool] = None
    has_hidden_subscriptions_on_profile: Optional[StrictBool] = None
    has_nft_avatar: Optional[StrictBool] = None
    highlights_info: Optional[UserHighlightsInfo] = None
    id: Annotated[str, Field(strict=True)]
    is_blue_verified: StrictBool
    is_profile_translatable: Optional[StrictBool] = None
    legacy: UserLegacy
    legacy_extended_profile: Optional[UserLegacyExtendedProfile] = None
    premium_gifting_eligible: Optional[StrictBool] = None
    professional: Optional[UserProfessional] = None
    profile_image_shape: StrictStr
    rest_id: Annotated[str, Field(strict=True)]
    super_follow_eligible: Optional[StrictBool] = None
    super_followed_by: Optional[StrictBool] = None
    super_following: Optional[StrictBool] = None
    tipjar_settings: Optional[UserTipJarSettings] = None
    user_seed_tweet_count: Optional[StrictInt] = None
    verification_info: Optional[UserVerificationInfo] = None
    __properties: ClassVar[List[str]] = ["__typename", "affiliates_highlighted_label", "business_account", "creator_subscriptions_count", "has_graduated_access", "has_hidden_likes_on_profile", "has_hidden_subscriptions_on_profile", "has_nft_avatar", "highlights_info", "id", "is_blue_verified", "is_profile_translatable", "legacy", "legacy_extended_profile", "premium_gifting_eligible", "professional", "profile_image_shape", "rest_id", "super_follow_eligible", "super_followed_by", "super_following", "tipjar_settings", "user_seed_tweet_count", "verification_info"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^([A-Za-z0-9+\/]{4})*([A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}==)?$", value):
            raise ValueError(r"must validate the regular expression /^([A-Za-z0-9+\/]{4})*([A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}==)?$/")
        return value

    @field_validator('profile_image_shape')
    def profile_image_shape_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Circle', 'Square', 'Hexagon']):
            raise ValueError("must be one of enum values ('Circle', 'Square', 'Hexagon')")
        return value

    @field_validator('rest_id')
    def rest_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of highlights_info
        if self.highlights_info:
            _dict['highlights_info'] = self.highlights_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legacy
        if self.legacy:
            _dict['legacy'] = self.legacy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legacy_extended_profile
        if self.legacy_extended_profile:
            _dict['legacy_extended_profile'] = self.legacy_extended_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of professional
        if self.professional:
            _dict['professional'] = self.professional.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tipjar_settings
        if self.tipjar_settings:
            _dict['tipjar_settings'] = self.tipjar_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification_info
        if self.verification_info:
            _dict['verification_info'] = self.verification_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "__typename": obj.get("__typename"),
            "affiliates_highlighted_label": obj.get("affiliates_highlighted_label"),
            "business_account": obj.get("business_account"),
            "creator_subscriptions_count": obj.get("creator_subscriptions_count"),
            "has_graduated_access": obj.get("has_graduated_access"),
            "has_hidden_likes_on_profile": obj.get("has_hidden_likes_on_profile"),
            "has_hidden_subscriptions_on_profile": obj.get("has_hidden_subscriptions_on_profile"),
            "has_nft_avatar": obj.get("has_nft_avatar"),
            "highlights_info": UserHighlightsInfo.from_dict(obj["highlights_info"]) if obj.get("highlights_info") is not None else None,
            "id": obj.get("id"),
            "is_blue_verified": obj.get("is_blue_verified"),
            "is_profile_translatable": obj.get("is_profile_translatable"),
            "legacy": UserLegacy.from_dict(obj["legacy"]) if obj.get("legacy") is not None else None,
            "legacy_extended_profile": UserLegacyExtendedProfile.from_dict(obj["legacy_extended_profile"]) if obj.get("legacy_extended_profile") is not None else None,
            "premium_gifting_eligible": obj.get("premium_gifting_eligible"),
            "professional": UserProfessional.from_dict(obj["professional"]) if obj.get("professional") is not None else None,
            "profile_image_shape": obj.get("profile_image_shape"),
            "rest_id": obj.get("rest_id"),
            "super_follow_eligible": obj.get("super_follow_eligible"),
            "super_followed_by": obj.get("super_followed_by"),
            "super_following": obj.get("super_following"),
            "tipjar_settings": UserTipJarSettings.from_dict(obj["tipjar_settings"]) if obj.get("tipjar_settings") is not None else None,
            "user_seed_tweet_count": obj.get("user_seed_tweet_count"),
            "verification_info": UserVerificationInfo.from_dict(obj["verification_info"]) if obj.get("verification_info") is not None else None
        })
        return _obj


