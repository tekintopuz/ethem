import json
import os

from django.utils.translation import gettext as _
from drf_yasg import openapi

from kint.settings import BASE_DIR

vendor_register_step_one_response_schema_dict = {
    400: "Bad Request",
    201: openapi.Response(
        description="Email address is verified successfully",
        examples={
            "application/json": {
                "success": True,
                "message": _("User's email was verified successfully."),
                "user_secret": "cwbz27d43qujz40x4jqeybuoq4vfaj1wwxrcthzk6i*****",
            }
        }
    ),
}

vendor_comments_mine_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Customer Own Comments",
        examples={
            "application/json": {

            }
        }
    ),
}

product_comments_mine_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Customer Own Comments",
        examples={
            "application/json": {

            }
        }
    ),
}
vendor_me_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Vendor Profile",
        examples={
            "application/json": {
                "success": True,
                "message": {
                    "id": 2,
                    "user": {
                        "id": 18,
                        "username": "vendor@kintshop.com",
                        "email": "vendor@kintshop.com",
                        "first_name": "Vendor",
                        "last_name": "Kintshop",
                        "avatar": None,
                        "phone": None,
                        "role": "vendor",
                        "is_email_verified": False,
                        "email_verified_at": "2022-11-30T09:35:33+03:00",
                        "is_mobile_verified": False,
                        "mobile_verified_at": None,
                        "date_joined": "2022-11-15T12:23:26+03:00",
                        "groups": [
                            {
                                "id": 3,
                                "name": "Vendor",
                                "permissions": []
                            }
                        ],
                        "user_permissions": [],
                        "kintshop_sms_allowed": True,
                        "kintshop_email_allowed": True,
                        "kintshop_phone_allowed": True,
                        "addresses": [],
                        "basket": {
                            "id": 4,
                            "products": [],
                            "amount": 0,
                            "total_price": None
                        }
                    },
                    "main_category": 2,
                    "status": "STEP-1",
                    "company_type": "Limited Şirketi",
                    "trade_name": None,
                    "trade_registration_number": None,
                    "store_name": None,
                    "vergi_dairesi": None,
                    "tckn": None,
                    "tax_number": None,
                    "kep_adresi": None,
                    "iban": None,
                    "mersis_number": None,
                    "invoice_type": None,
                    "links": "",
                    "finance_name": None,
                    "operation_name": None,
                    "finance_phone": None,
                    "operation_phone": None,
                    "finance_email": None,
                    "operation_email": None,
                    "activation_code": None,
                    "is_active": True,
                    "is_approved": False,
                    "is_completed": False,
                    "is_situation": False,
                    "no_sales": False,
                    "personal_data": False,
                    "agreement": False,
                    "check_agreement": False,
                    "invoice_address": None,
                    "company_address": None,
                    "shop_address": None,
                    "shippment_address": None,
                    "return_address": None,
                    "logo": {
                        "slug": "",
                        "thumbnail": "",
                        "original": ""
                    },
                    "remember_token": None,
                    "number_of_followers": 1,
                    "shipment_company": 1,
                    "background_image": None,
                    "background_color": "#00EEFF",
                    "background_active": True,
                    "font_color": "#00EEFF",
                    "created_at": "2022-11-23T16:52:20.533018+03:00",
                    "files": []
                }
            }
        }
    ),
}

sss_entry_response_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    200: openapi.Response(
        description="New SSS Entry is added in SSS title",
        examples={
            "application/json": {
                "success": True,
                "message": _("new sss_entry is created successfully successfully."),
            }
        }
    ),
}
vendor_register_step_two_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Vendor registration step two (Email Verification Code)",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor verified its email successfully."),
            }
        }
    ),
}

basket_get_response_schema_dict = {
    500: "Internal Server Error",
    200: openapi.Response(
        description="Authenticated User Basket",
        examples={
            "application/json": {
                "id": 1,
                "products": [
                    {
                        "id": 2,
                        "product": {
                            "id": 17,
                            "vendor": 5,
                            "vendor_user": {
                                "id": 43,
                                "username": "av.tekintopuz@gmail.com",
                                "email": "av.tekintopuz@gmail.com",
                                "first_name": "Tekin",
                                "last_name": "TOPUZ",
                                "avatar": None,
                                "phone": "+905536858122",
                                "role": "vendor",
                                "is_email_verified": True,
                                "email_verified_at": None,
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-12-02T12:03:31+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [
                                    {
                                        "id": 21,
                                        "owner": 43,
                                        "title": "Company Address",
                                        "country": "Turkey",
                                        "state": None,
                                        "city": None,
                                        "il": "Ankara",
                                        "ilce": "Altındağ",
                                        "semt": "Hasköy",
                                        "mahalle_koy": "Güneşevler Mah.",
                                        "street_address": "",
                                        "first_name": "Tekin",
                                        "last_name": "TOPUZ",
                                        "mobile_phone": None,
                                        "tckn": None,
                                        "pasaport_no": None,
                                        "is_active": True,
                                        "is_current": False,
                                        "postal_code": None
                                    }
                                ],
                                "vendor": {
                                    "id": 5,
                                    "status": "STEP-4",
                                    "company_type": "Anonim Şirket",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": "Topuz Soft",
                                    "tckn": "17501613172",
                                    "tax_number": "1750161317",
                                    "kep_adresi": "asdasdasdasd",
                                    "iban": "TR33BUKB20201555555552",
                                    "mersis_number": None,
                                    "invoice_type": "E-Arşiv Fatura",
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:31.156944+03:00",
                                    "created_at": "2022-12-02T12:03:31.866733+03:00",
                                    "user": 43,
                                    "main_category": 2,
                                    "vergi_dairesi": 74,
                                    "invoice_address": None,
                                    "company_address": 21,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": [
                                        {
                                            "id": 2,
                                            "status": "pending",
                                            "title": "Ruhsat Belgesi",
                                            "detail": "Altındağ Belediyesi tarafından verilen işyeri açma ruhsatı.",
                                            "is_active": True,
                                            "is_deleted": False,
                                            "deleted_at": None,
                                            "updated_at": "2022-12-05T15:29:56.143194+03:00",
                                            "created_at": "2022-12-05T15:29:56.143194+03:00",
                                            "vendor": 5,
                                            "attachment": {
                                                "id": 294,
                                                "slug": "isyeri-acma-ruhsat",
                                                "thumbnail": "http://65.109.128.137:9000/images/20221205/vendor/thumbnail_2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg",
                                                "original": "http://65.109.128.137:9000/images/20221205/vendor/2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg"
                                            },
                                            "deleted_by": None,
                                            "created_by": 14
                                        }
                                    ]
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Av. Tekin Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "12313561215",
                            "description": "Variant",
                            "image": {
                                "id": 274,
                                "slug": "akbank",
                                "thumbnail": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png",
                                "original": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png"
                            },
                            "galery": [
                                {
                                    "id": 105,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/iq.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/iq.svg"
                                },
                                {
                                    "id": 104,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ir.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ir.svg"
                                },
                                {
                                    "id": 103,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/id.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/id.svg"
                                },
                                {
                                    "id": 102,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/in.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/in.svg"
                                },
                                {
                                    "id": 100,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/hu.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/hu.svg"
                                }
                            ],
                            "is_published": False,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code11",
                            "kdv": 0.0,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "100.00",
                            "kintshop_price": "0.00",
                            "net_price": "100.00",
                            "discount": 0.0,
                            "prices": [
                                {
                                    "id": 22,
                                    "discount": 100.0,
                                    "kintshop_price": "100.00",
                                    "gross_price": "100.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:09:57.581738+03:00",
                                    "updated_at": "2022-12-05T17:09:57.581738+03:00",
                                    "deleted_at": None,
                                    "product": 17,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 22,
                            "discount": 100.0,
                            "kintshop_price": "100.00",
                            "gross_price": "100.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:09:57.581738+03:00",
                            "updated_at": "2022-12-05T17:09:57.581738+03:00",
                            "deleted_at": None,
                            "product": 17,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "400.00",
                        "amount": 4,
                        "created_at": "2022-12-07T09:55:10.945393+03:00"
                    },
                    {
                        "id": 3,
                        "product": {
                            "id": 18,
                            "vendor": 2,
                            "vendor_user": {
                                "id": 18,
                                "username": "vendor@kintshop.com",
                                "email": "vendor@kintshop.com",
                                "first_name": "Vendor",
                                "last_name": "Kintshop",
                                "avatar": None,
                                "phone": None,
                                "role": "vendor",
                                "is_email_verified": False,
                                "email_verified_at": "2022-11-30T09:35:33+03:00",
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-11-15T12:23:26+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [],
                                "vendor": {
                                    "id": 2,
                                    "status": "STEP-1",
                                    "company_type": "Limited Şirketi",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": None,
                                    "tckn": None,
                                    "tax_number": None,
                                    "kep_adresi": None,
                                    "iban": None,
                                    "mersis_number": None,
                                    "invoice_type": None,
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:21.492398+03:00",
                                    "created_at": "2022-11-23T16:52:20.533018+03:00",
                                    "user": 18,
                                    "main_category": 2,
                                    "vergi_dairesi": None,
                                    "invoice_address": None,
                                    "company_address": None,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": []
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "1231312",
                            "description": "string Product-1 Product-1Product-1",
                            "image": {
                                "id": 267,
                                "slug": "xxxx",
                                "thumbnail": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg",
                                "original": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg"
                            },
                            "galery": [
                                {
                                    "id": 5,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/as.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/as.svg"
                                },
                                {
                                    "id": 4,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/dz.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/dz.svg"
                                },
                                {
                                    "id": 3,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/al.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/al.svg"
                                },
                                {
                                    "id": 2,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ax.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ax.svg"
                                },
                                {
                                    "id": 1,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/af.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/af.svg"
                                }
                            ],
                            "is_published": True,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code",
                            "kdv": 0.1,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "250.00",
                            "kintshop_price": "200.00",
                            "net_price": "225.00",
                            "discount": 10.0,
                            "prices": [
                                {
                                    "id": 23,
                                    "discount": 10.0,
                                    "kintshop_price": "200.00",
                                    "gross_price": "250.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:58:11.464732+03:00",
                                    "updated_at": "2022-12-05T17:58:11.464732+03:00",
                                    "deleted_at": None,
                                    "product": 18,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 23,
                            "discount": 10.0,
                            "kintshop_price": "200.00",
                            "gross_price": "250.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:58:11.464732+03:00",
                            "updated_at": "2022-12-05T17:58:11.464732+03:00",
                            "deleted_at": None,
                            "product": 18,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "800.00",
                        "amount": 4,
                        "created_at": "2022-12-07T10:16:01.976914+03:00"
                    }
                ],
                "amount": 8,
                "total_price": "1200.00"
            }
        }
    ),
}
basket_post_response_schema_dict = {
    500: "Internal Server Error",
    200: "Basket Contents",
    201: openapi.Response(
        description="Authenticated User Basket",
        examples={
            "application/json": {
                "id": 1,
                "products": [
                    {
                        "id": 2,
                        "product": {
                            "id": 17,
                            "vendor": 5,
                            "vendor_user": {
                                "id": 43,
                                "username": "av.tekintopuz@gmail.com",
                                "email": "av.tekintopuz@gmail.com",
                                "first_name": "Tekin",
                                "last_name": "TOPUZ",
                                "avatar": None,
                                "phone": "+905536858122",
                                "role": "vendor",
                                "is_email_verified": True,
                                "email_verified_at": None,
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-12-02T12:03:31+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [
                                    {
                                        "id": 21,
                                        "owner": 43,
                                        "title": "Company Address",
                                        "country": "Turkey",
                                        "state": None,
                                        "city": None,
                                        "il": "Ankara",
                                        "ilce": "Altındağ",
                                        "semt": "Hasköy",
                                        "mahalle_koy": "Güneşevler Mah.",
                                        "street_address": "",
                                        "first_name": "Tekin",
                                        "last_name": "TOPUZ",
                                        "mobile_phone": None,
                                        "tckn": None,
                                        "pasaport_no": None,
                                        "is_active": True,
                                        "is_current": False,
                                        "postal_code": None
                                    }
                                ],
                                "vendor": {
                                    "id": 5,
                                    "status": "STEP-4",
                                    "company_type": "Anonim Şirket",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": "Topuz Soft",
                                    "tckn": "17501613172",
                                    "tax_number": "1750161317",
                                    "kep_adresi": "asdasdasdasd",
                                    "iban": "TR33BUKB20201555555552",
                                    "mersis_number": None,
                                    "invoice_type": "E-Arşiv Fatura",
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:31.156944+03:00",
                                    "created_at": "2022-12-02T12:03:31.866733+03:00",
                                    "user": 43,
                                    "main_category": 2,
                                    "vergi_dairesi": 74,
                                    "invoice_address": None,
                                    "company_address": 21,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": [
                                        {
                                            "id": 2,
                                            "status": "pending",
                                            "title": "Ruhsat Belgesi",
                                            "detail": "Altındağ Belediyesi tarafından verilen işyeri açma ruhsatı.",
                                            "is_active": True,
                                            "is_deleted": False,
                                            "deleted_at": None,
                                            "updated_at": "2022-12-05T15:29:56.143194+03:00",
                                            "created_at": "2022-12-05T15:29:56.143194+03:00",
                                            "vendor": 5,
                                            "attachment": {
                                                "id": 294,
                                                "slug": "isyeri-acma-ruhsat",
                                                "thumbnail": "http://65.109.128.137:9000/images/20221205/vendor/thumbnail_2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg",
                                                "original": "http://65.109.128.137:9000/images/20221205/vendor/2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg"
                                            },
                                            "deleted_by": None,
                                            "created_by": 14
                                        }
                                    ]
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Av. Tekin Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "12313561215",
                            "description": "Variant",
                            "image": {
                                "id": 274,
                                "slug": "akbank",
                                "thumbnail": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png",
                                "original": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png"
                            },
                            "galery": [
                                {
                                    "id": 105,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/iq.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/iq.svg"
                                },
                                {
                                    "id": 104,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ir.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ir.svg"
                                },
                                {
                                    "id": 103,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/id.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/id.svg"
                                },
                                {
                                    "id": 102,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/in.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/in.svg"
                                },
                                {
                                    "id": 100,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/hu.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/hu.svg"
                                }
                            ],
                            "is_published": False,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code11",
                            "kdv": 0.0,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "100.00",
                            "kintshop_price": "0.00",
                            "net_price": "100.00",
                            "discount": 0.0,
                            "prices": [
                                {
                                    "id": 22,
                                    "discount": 100.0,
                                    "kintshop_price": "100.00",
                                    "gross_price": "100.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:09:57.581738+03:00",
                                    "updated_at": "2022-12-05T17:09:57.581738+03:00",
                                    "deleted_at": None,
                                    "product": 17,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 22,
                            "discount": 100.0,
                            "kintshop_price": "100.00",
                            "gross_price": "100.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:09:57.581738+03:00",
                            "updated_at": "2022-12-05T17:09:57.581738+03:00",
                            "deleted_at": None,
                            "product": 17,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "400.00",
                        "amount": 4,
                        "created_at": "2022-12-07T09:55:10.945393+03:00"
                    },
                    {
                        "id": 3,
                        "product": {
                            "id": 18,
                            "vendor": 2,
                            "vendor_user": {
                                "id": 18,
                                "username": "vendor@kintshop.com",
                                "email": "vendor@kintshop.com",
                                "first_name": "Vendor",
                                "last_name": "Kintshop",
                                "avatar": None,
                                "phone": None,
                                "role": "vendor",
                                "is_email_verified": False,
                                "email_verified_at": "2022-11-30T09:35:33+03:00",
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-11-15T12:23:26+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [],
                                "vendor": {
                                    "id": 2,
                                    "status": "STEP-1",
                                    "company_type": "Limited Şirketi",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": None,
                                    "tckn": None,
                                    "tax_number": None,
                                    "kep_adresi": None,
                                    "iban": None,
                                    "mersis_number": None,
                                    "invoice_type": None,
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:21.492398+03:00",
                                    "created_at": "2022-11-23T16:52:20.533018+03:00",
                                    "user": 18,
                                    "main_category": 2,
                                    "vergi_dairesi": None,
                                    "invoice_address": None,
                                    "company_address": None,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": []
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "1231312",
                            "description": "string Product-1 Product-1Product-1",
                            "image": {
                                "id": 267,
                                "slug": "xxxx",
                                "thumbnail": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg",
                                "original": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg"
                            },
                            "galery": [
                                {
                                    "id": 5,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/as.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/as.svg"
                                },
                                {
                                    "id": 4,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/dz.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/dz.svg"
                                },
                                {
                                    "id": 3,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/al.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/al.svg"
                                },
                                {
                                    "id": 2,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ax.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ax.svg"
                                },
                                {
                                    "id": 1,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/af.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/af.svg"
                                }
                            ],
                            "is_published": True,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code",
                            "kdv": 0.1,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "250.00",
                            "kintshop_price": "200.00",
                            "net_price": "225.00",
                            "discount": 10.0,
                            "prices": [
                                {
                                    "id": 23,
                                    "discount": 10.0,
                                    "kintshop_price": "200.00",
                                    "gross_price": "250.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:58:11.464732+03:00",
                                    "updated_at": "2022-12-05T17:58:11.464732+03:00",
                                    "deleted_at": None,
                                    "product": 18,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 23,
                            "discount": 10.0,
                            "kintshop_price": "200.00",
                            "gross_price": "250.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:58:11.464732+03:00",
                            "updated_at": "2022-12-05T17:58:11.464732+03:00",
                            "deleted_at": None,
                            "product": 18,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "800.00",
                        "amount": 4,
                        "created_at": "2022-12-07T10:16:01.976914+03:00"
                    }
                ],
                "amount": 8,
                "total_price": "1200.00"
            }
        }
    ),
}

basket_delete_response_schema_dict = {
    500: "Internal Server Error",
    204: openapi.Response(
        description="Authenticated User Basket",
        examples={
            "application/json": {
                "id": 1,
                "products": [
                    {
                        "id": 2,
                        "product": {
                            "id": 17,
                            "vendor": 5,
                            "vendor_user": {
                                "id": 43,
                                "username": "av.tekintopuz@gmail.com",
                                "email": "av.tekintopuz@gmail.com",
                                "first_name": "Tekin",
                                "last_name": "TOPUZ",
                                "avatar": None,
                                "phone": "+905536858122",
                                "role": "vendor",
                                "is_email_verified": True,
                                "email_verified_at": None,
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-12-02T12:03:31+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [
                                    {
                                        "id": 21,
                                        "owner": 43,
                                        "title": "Company Address",
                                        "country": "Turkey",
                                        "state": None,
                                        "city": None,
                                        "il": "Ankara",
                                        "ilce": "Altındağ",
                                        "semt": "Hasköy",
                                        "mahalle_koy": "Güneşevler Mah.",
                                        "street_address": "",
                                        "first_name": "Tekin",
                                        "last_name": "TOPUZ",
                                        "mobile_phone": None,
                                        "tckn": None,
                                        "pasaport_no": None,
                                        "is_active": True,
                                        "is_current": False,
                                        "postal_code": None
                                    }
                                ],
                                "vendor": {
                                    "id": 5,
                                    "status": "STEP-4",
                                    "company_type": "Anonim Şirket",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": "Topuz Soft",
                                    "tckn": "17501613172",
                                    "tax_number": "1750161317",
                                    "kep_adresi": "asdasdasdasd",
                                    "iban": "TR33BUKB20201555555552",
                                    "mersis_number": None,
                                    "invoice_type": "E-Arşiv Fatura",
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:31.156944+03:00",
                                    "created_at": "2022-12-02T12:03:31.866733+03:00",
                                    "user": 43,
                                    "main_category": 2,
                                    "vergi_dairesi": 74,
                                    "invoice_address": None,
                                    "company_address": 21,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": [
                                        {
                                            "id": 2,
                                            "status": "pending",
                                            "title": "Ruhsat Belgesi",
                                            "detail": "Altındağ Belediyesi tarafından verilen işyeri açma ruhsatı.",
                                            "is_active": True,
                                            "is_deleted": False,
                                            "deleted_at": None,
                                            "updated_at": "2022-12-05T15:29:56.143194+03:00",
                                            "created_at": "2022-12-05T15:29:56.143194+03:00",
                                            "vendor": 5,
                                            "attachment": {
                                                "id": 294,
                                                "slug": "isyeri-acma-ruhsat",
                                                "thumbnail": "http://65.109.128.137:9000/images/20221205/vendor/thumbnail_2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg",
                                                "original": "http://65.109.128.137:9000/images/20221205/vendor/2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg"
                                            },
                                            "deleted_by": None,
                                            "created_by": 14
                                        }
                                    ]
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Av. Tekin Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "12313561215",
                            "description": "Variant",
                            "image": {
                                "id": 274,
                                "slug": "akbank",
                                "thumbnail": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png",
                                "original": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png"
                            },
                            "galery": [
                                {
                                    "id": 105,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/iq.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/iq.svg"
                                },
                                {
                                    "id": 104,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ir.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ir.svg"
                                },
                                {
                                    "id": 103,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/id.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/id.svg"
                                },
                                {
                                    "id": 102,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/in.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/in.svg"
                                },
                                {
                                    "id": 100,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/hu.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/hu.svg"
                                }
                            ],
                            "is_published": False,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code11",
                            "kdv": 0.0,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "100.00",
                            "kintshop_price": "0.00",
                            "net_price": "100.00",
                            "discount": 0.0,
                            "prices": [
                                {
                                    "id": 22,
                                    "discount": 100.0,
                                    "kintshop_price": "100.00",
                                    "gross_price": "100.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:09:57.581738+03:00",
                                    "updated_at": "2022-12-05T17:09:57.581738+03:00",
                                    "deleted_at": None,
                                    "product": 17,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 22,
                            "discount": 100.0,
                            "kintshop_price": "100.00",
                            "gross_price": "100.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:09:57.581738+03:00",
                            "updated_at": "2022-12-05T17:09:57.581738+03:00",
                            "deleted_at": None,
                            "product": 17,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "400.00",
                        "amount": 4,
                        "created_at": "2022-12-07T09:55:10.945393+03:00"
                    },
                    {
                        "id": 3,
                        "product": {
                            "id": 18,
                            "vendor": 2,
                            "vendor_user": {
                                "id": 18,
                                "username": "vendor@kintshop.com",
                                "email": "vendor@kintshop.com",
                                "first_name": "Vendor",
                                "last_name": "Kintshop",
                                "avatar": None,
                                "phone": None,
                                "role": "vendor",
                                "is_email_verified": False,
                                "email_verified_at": "2022-11-30T09:35:33+03:00",
                                "is_mobile_verified": False,
                                "mobile_verified_at": None,
                                "date_joined": "2022-11-15T12:23:26+03:00",
                                "groups": [
                                    3
                                ],
                                "user_permissions": [],
                                "addresses": [],
                                "vendor": {
                                    "id": 2,
                                    "status": "STEP-1",
                                    "company_type": "Limited Şirketi",
                                    "reference_code": None,
                                    "trade_name": None,
                                    "trade_registration_number": None,
                                    "store_name": None,
                                    "tckn": None,
                                    "tax_number": None,
                                    "kep_adresi": None,
                                    "iban": None,
                                    "mersis_number": None,
                                    "invoice_type": None,
                                    "links": "",
                                    "finance_name": None,
                                    "operation_name": None,
                                    "finance_phone": None,
                                    "operation_phone": None,
                                    "finance_email": None,
                                    "operation_email": None,
                                    "activation_code": None,
                                    "is_active": True,
                                    "is_approved": False,
                                    "is_completed": False,
                                    "is_situation": False,
                                    "no_sales": False,
                                    "personal_data": False,
                                    "agreement": False,
                                    "check_agreement": False,
                                    "logo": None,
                                    "remember_token": None,
                                    "tax_administration_id": 1,
                                    "shipment_company": 1,
                                    "background_image": None,
                                    "background_color": "#00EEFF",
                                    "background_active": True,
                                    "font_color": "#00EEFF",
                                    "is_deleted": False,
                                    "deleted_at": None,
                                    "updated_at": "2022-12-05T12:36:21.492398+03:00",
                                    "created_at": "2022-11-23T16:52:20.533018+03:00",
                                    "user": 18,
                                    "main_category": 2,
                                    "vergi_dairesi": None,
                                    "invoice_address": None,
                                    "company_address": None,
                                    "shop_address": None,
                                    "shippment_address": None,
                                    "return_address": None,
                                    "deleted_by": None,
                                    "created_by": None,
                                    "files": []
                                },
                                "is_superuser": False,
                                "is_staff": False
                            },
                            "brand": "Hummer",
                            "model": "Product-1",
                            "title": "Product-1",
                            "name": "Product-1",
                            "barcode": "1231312",
                            "description": "string Product-1 Product-1Product-1",
                            "image": {
                                "id": 267,
                                "slug": "xxxx",
                                "thumbnail": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg",
                                "original": "http://65.109.128.137:9000/images20221123/product2022_11_23_08_44_08_xxxx.jpg"
                            },
                            "galery": [
                                {
                                    "id": 5,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/as.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/as.svg"
                                },
                                {
                                    "id": 4,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/dz.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/dz.svg"
                                },
                                {
                                    "id": 3,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/al.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/al.svg"
                                },
                                {
                                    "id": 2,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ax.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/ax.svg"
                                },
                                {
                                    "id": 1,
                                    "slug": None,
                                    "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/af.svg",
                                    "original": "http://65.109.128.137:9000/images/flags/originals/af.svg"
                                }
                            ],
                            "is_published": True,
                            "comments": [],
                            "category": "Elektronik",
                            "categories": None,
                            "stock": 20,
                            "stock_code": "stock-code",
                            "kdv": 0.1,
                            "delivery_time": "Morning",
                            "specs": [],
                            "is_reviewed": False,
                            "reviewed_by": None,
                            "reviewed_at": None,
                            "variants": [],
                            "parent": None,
                            "avg_rate": 0.0,
                            "total_comments": 0,
                            "comment_statistics": {},
                            "in_mainpage": False,
                            "status": "pending",
                            "feedbacks": [],
                            "hits": 0,
                            "slug": "product-1",
                            "gross_price": "250.00",
                            "kintshop_price": "200.00",
                            "net_price": "225.00",
                            "discount": 10.0,
                            "prices": [
                                {
                                    "id": 23,
                                    "discount": 10.0,
                                    "kintshop_price": "200.00",
                                    "gross_price": "250.00",
                                    "net_price": None,
                                    "currency": "TRY",
                                    "is_active": True,
                                    "is_deleted": False,
                                    "created_at": "2022-12-05T17:58:11.464732+03:00",
                                    "updated_at": "2022-12-05T17:58:11.464732+03:00",
                                    "deleted_at": None,
                                    "product": 18,
                                    "deleted_by": None,
                                    "created_by": None
                                }
                            ]
                        },
                        "price": {
                            "id": 23,
                            "discount": 10.0,
                            "kintshop_price": "200.00",
                            "gross_price": "250.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:58:11.464732+03:00",
                            "updated_at": "2022-12-05T17:58:11.464732+03:00",
                            "deleted_at": None,
                            "product": 18,
                            "deleted_by": None,
                            "created_by": None
                        },
                        "total_price": "800.00",
                        "amount": 4,
                        "created_at": "2022-12-07T10:16:01.976914+03:00"
                    }
                ],
                "amount": 8,
                "total_price": "1200.00"
            }
        }
    ),
}
vendor_register_step_three_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Vendor registration password set",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor-user's password is set successfully."),
            }
        }
    ),
}
vendor_company_info_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Vendor company info",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor company's info is set successfully."),
            }
        }
    ),
}
category_remove_variant_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'variant': openapi.Schema(type=openapi.TYPE_INTEGER, description='You can send individual id or a list of ids')
    })
category_remove_spec_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'spec': openapi.Schema(type=openapi.TYPE_INTEGER, description='You can send individual id or a list of ids')
    })
product_galery_remove_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'attachment': openapi.Schema(type=openapi.TYPE_INTEGER,
                                     description='You can send indiviual id or a list of ids')
    })

product_galery_remove_response_schema_dict = {
    500: "Internal Server Error",
    400: "Bad Request",
    204: openapi.Response(
        description="Deletion is successful",
        examples={
            "application/json": {"status": "success",
                                 "message": "Attachement removed from galery"
                                 }
        }
    )
}

product_favourite_response_schema_dict = {
    500: "Internal Server Error",
    400: "Bad Request",
    204: openapi.Response(
        description="Product is removed from user favourite list.",
        examples={
            "application/json": {"status": "success",
                                 "message": _("Product is removed from user favourite list!")}
        }
    ),
    201: openapi.Response(
        description="Product is added into user favourite list.",
        examples={
            "application/json": {
                "id": 6,
                "product": {
                    "id": 17,
                    "vendor": {
                        "id": 5,
                        "status": "STEP-4",
                        "company_type": "Anonim Şirket",
                        "reference_code": None,
                        "trade_name": None,
                        "trade_registration_number": None,
                        "store_name": "Topuz Soft",
                        "tckn": "17501613172",
                        "tax_number": "1750161317",
                        "kep_adresi": "asdasdasdasd",
                        "iban": "TR33BUKB20201555555552",
                        "mersis_number": None,
                        "invoice_type": "E-Arşiv Fatura",
                        "links": "",
                        "finance_name": None,
                        "operation_name": None,
                        "finance_phone": None,
                        "operation_phone": None,
                        "finance_email": None,
                        "operation_email": None,
                        "activation_code": None,
                        "is_active": True,
                        "is_approved": False,
                        "is_completed": False,
                        "is_situation": False,
                        "no_sales": False,
                        "personal_data": False,
                        "agreement": False,
                        "check_agreement": False,
                        "logo": None,
                        "remember_token": None,
                        "tax_administration_id": 1,
                        "shipment_company": 1,
                        "background_image": None,
                        "background_color": "#00EEFF",
                        "background_active": True,
                        "font_color": "#00EEFF",
                        "is_deleted": False,
                        "deleted_at": None,
                        "updated_at": "2022-12-05T12:36:31.156944+03:00",
                        "created_at": "2022-12-02T12:03:31.866733+03:00",
                        "user": 43,
                        "main_category": 2,
                        "vergi_dairesi": 74,
                        "invoice_address": None,
                        "company_address": 21,
                        "shop_address": None,
                        "shippment_address": None,
                        "return_address": None,
                        "deleted_by": None,
                        "created_by": None,
                        "files": [
                            {
                                "id": 2,
                                "status": "pending",
                                "title": "Ruhsat Belgesi",
                                "detail": "Altındağ Belediyesi tarafından verilen işyeri açma ruhsatı.",
                                "is_active": True,
                                "is_deleted": False,
                                "deleted_at": None,
                                "updated_at": "2022-12-05T15:29:56.143194+03:00",
                                "created_at": "2022-12-05T15:29:56.143194+03:00",
                                "vendor": 5,
                                "attachment": {
                                    "id": 294,
                                    "slug": "isyeri-acma-ruhsat",
                                    "thumbnail": "http://65.109.128.137:9000/images/20221205/vendor/thumbnail_2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg",
                                    "original": "http://65.109.128.137:9000/images/20221205/vendor/2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg"
                                },
                                "deleted_by": None,
                                "created_by": 14
                            }
                        ]
                    },
                    "brand": "Hummer",
                    "model": "Av. Tekin Product-1",
                    "title": "Product-1",
                    "name": "Product-1",
                    "barcode": "12313561215",
                    "description": "Variant",
                    "source": None,
                    "image": {
                        "id": 274,
                        "slug": "akbank",
                        "thumbnail": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png",
                        "original": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png"
                    },
                    "galery": [
                        {
                            "id": 105,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/iq.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/iq.svg"
                        },
                        {
                            "id": 104,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ir.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/ir.svg"
                        },
                        {
                            "id": 103,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/id.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/id.svg"
                        },
                        {
                            "id": 102,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/in.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/in.svg"
                        },
                        {
                            "id": 100,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/hu.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/hu.svg"
                        }
                    ],
                    "is_published": False,
                    "comments": [],
                    "category": "Elektronik",
                    "categories": None,
                    "stock": 20,
                    "stock_code": "stock-code11",
                    "kdv": 0,
                    "delivery_time": "Morning",
                    "specs": [],
                    "is_reviewed": False,
                    "reviewed_by": None,
                    "reviewed_at": None,
                    "variants": [],
                    "parent": None,
                    "avg_rate": 0,
                    "total_comments": 0,
                    "comment_statistics": {},
                    "in_mainpage": False,
                    "status": "pending",
                    "feedbacks": [],
                    "hits": 0,
                    "slug": "product-1",
                    "gross_price": "100.00",
                    "kintshop_price": "0.00",
                    "net_price": "100.00",
                    "discount": 0,
                    "prices": [
                        {
                            "id": 22,
                            "discount": 100,
                            "kintshop_price": "100.00",
                            "gross_price": "100.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:09:57.581738+03:00",
                            "updated_at": "2022-12-05T17:09:57.581738+03:00",
                            "deleted_at": None,
                            "product": 17,
                            "deleted_by": None,
                            "created_by": None
                        }
                    ]
                },
                "created_by": {
                    "id": 27,
                    "username": "c.topuz@yahoo.com",
                    "email": "c.topuz@yahoo.com",
                    "first_name": "Tekin",
                    "last_name": "TOPUZ",
                    "avatar": None,
                    "phone": None,
                    "role": "customer",
                    "is_email_verified": True,
                    "email_verified_at": "2022-11-30T09:31:29+03:00",
                    "is_mobile_verified": True,
                    "mobile_verified_at": None,
                    "date_joined": "2022-11-30T09:30:55+03:00",
                    "groups": [
                        {
                            "id": 1,
                            "name": "Customer",
                            "permissions": []
                        }
                    ],
                    "user_permissions": []
                },
                "price": None
            }
        }
    )
}

category_add_new_spec_response_schema_dict = {
    500: "Internal Server Error",
    400: "Bad Request",
    201: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                "id": 4610,
                "spec": {
                    "id": 21,
                    "type": "variable",
                    "name": "Deneme 5/12/2022",
                    "slug": "deneme-5122022",
                    "values": [
                        {
                            "id": 45,
                            "value": "Variable-1",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 46,
                            "value": "Variable-2",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 47,
                            "value": "Variable-3",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        }
                    ]
                },
                "category": 2
            }
        }
    )
}

category_add_new_variant_response_schema_dict = {
    500: "Internal Server Error",
    400: "Bad Request",
    201: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                "id": 4610,
                "spec": {
                    "id": 21,
                    "type": "variable",
                    "name": "Deneme 5/12/2022",
                    "slug": "deneme-5122022",
                    "values": [
                        {
                            "id": 45,
                            "value": "Variable-1",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 46,
                            "value": "Variable-2",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 47,
                            "value": "Variable-3",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        }
                    ]
                },
                "category": 2
            }
        }
    )
}

token_response_schema_dict = {
    400: "Bad Request",
    201: openapi.Response(
        description="New JWT (JSON Web Token) is created successfully",
        examples={
            "application/json": {
                "refresh": "eyJhbG.eyJ0b2tlblY2QwZjVmYyIsInVzZXJfaWQiOjE4fQ.LPt_XnLC6KWtNE",
                "access": "eyJhbVCJ9.eyJ0b2tlbl9Dc2LCJpYXQiOjE2NjXNlcl9pZCI6MTh9.K6UPz8V0LTxm3qnI",
            }
        }
    )
}

register_response_schema_dict = {
    400: "Bad Request",
    201: openapi.Response(
        description="New User is created "
                    "successfully",
        examples={
            "application/json": {
                "access": "JWT TOKEN",
                "refresh": "Refresh TOKEN",
            }
        }
    ),
}

verification_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'token': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    })

verification_response_schema_dict = {
    400: "Bad Request",
    200: openapi.Response(
        description="Email address is verified successfully",
        examples={
            "application/json": {
                "success": True,
                "message": _("User's email was verified successfully.")
            }
        }
    ),
}

upload_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/x-www-form-urlencoded",
    properties={
        'type': openapi.Schema(type=openapi.TYPE_STRING, description='string: type of action eg. category, avatar'),
        'key': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'file': openapi.Schema(type=openapi.TYPE_FILE, description='file'),
    })

upload_response_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 262,
                    "thumbnail": None,
                    "original": "https://cdn.kintshop.com/images/20221118/2022_11_18_09_16_45_xxxx.png"
                }
            ]
        }
    ),
}

category_post_response_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 5527,
                    "title": "Deneme Catagory",
                    "slug": "deneme-category",
                    "parent": {
                        "id": 2374,
                        "title": "Kompresör",
                        "slug": "kompresor",
                        "parent": {
                            "id": 104,
                            "title": "Aksesuar & Yedek Parça",
                            "slug": "aksesuar-yedek-parca",
                            "parent": {
                                "id": 76,
                                "title": "Bilgisayar",
                                "slug": "bilgisayar",
                                "parent": {
                                    "id": 2,
                                    "title": "Elektronik",
                                    "slug": "elektronik",
                                    "parent": None,
                                    "galery": [],
                                    "bread_crump": "Elektronik",
                                    "specs": [
                                        {
                                            "id": 1,
                                            "spec": {
                                                "id": 1,
                                                "type": "variable",
                                                "name": "Renk",
                                                "slug": "renk",
                                                "values": [
                                                    {
                                                        "id": 1,
                                                        "value": "Beyaz",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 2,
                                                        "value": "Siyah",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 3,
                                                        "value": "Kırmızı",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 4,
                                                        "value": "Mavi",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 5,
                                                        "value": "Yeşil",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 6,
                                                        "value": "Sarı",
                                                        "image": None
                                                    },
                                                    {
                                                        "id": 7,
                                                        "value": "Mor",
                                                        "image": None
                                                    }
                                                ]
                                            }
                                        }
                                    ],
                                    "in_mainpage": True
                                },
                                "galery": [],
                                "bread_crump": "Elektronik | Bilgisayar",
                                "specs": [],
                                "in_mainpage": True
                            },
                            "galery": [],
                            "bread_crump": "Elektronik | Bilgisayar | Aksesuar & Yedek Parça",
                            "specs": [],
                            "in_mainpage": True
                        },
                        "galery": [],
                        "bread_crump": "Elektronik | Bilgisayar | Aksesuar & Yedek Parça | Kompresör",
                        "specs": [],
                        "in_mainpage": True
                    },
                    "bread_crump": "Deneme Category",
                    "sub_categories": [],
                    "specs": [],
                    "galery": [],
                    "in_mainpage": True
                }
            ]
        }
    ),
}
# Opening JSON file
f = open(os.path.join(BASE_DIR, 'utils', 'data', 'product_response.json'))
product_json = json.load(f)
product_dict = {}
for k, v in product_json.items():
    if type(k) is int:
        product_dict[k] = openapi.Schema(type=openapi.TYPE_INTEGER, description=f"title: {k}\nreadOnly: True")
    elif type(k) is str:
        product_dict[k] = openapi.Schema(type=openapi.TYPE_STRING, description=f"title: {k}\nreadOnly: True")
    elif type(k) is dict:
        product_dict[k] = openapi.Schema(type=openapi.TYPE_OBJECT, description=k)
    elif type(k) is list:
        product_dict[k] = openapi.Schema(type=openapi.TYPE_ARRAY, description=k)
    elif type(k) is bool:
        product_dict[k] = openapi.Schema(type=openapi.TYPE_BOOLEAN, description=k)

product_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/x-www-form-urlencoded",
    properties=product_dict)

product_response_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    201: openapi.Response(
        description="Product is created successfully",
        examples={
            "application/json": [
                product_json
            ]
        }
    ),
}

product_put_response_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    200: openapi.Response(
        description="Product is updated successfully",
        examples={
            "application/json": [
                product_json
            ]
        }
    ),
}

product_favourite_schema_dict = {
    400: "Bad Request",
    500: "Internal Server Error",
    200: openapi.Response(
        description="Product is added into user favourite product list successfully",
        examples={
            "application/json": [
                {

                    "id": 5527,
                    "title": "Deneme Catagory",
                    "slug": "deneme-category",
                }
            ]

        }
    ),
}
product_favourite_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/x-www-form-urlencoded")
