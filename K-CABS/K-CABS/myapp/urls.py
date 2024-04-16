
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.log_post),

    path('admins_home/',views.home),

    path('admins_add_driver/',views.admins_add_driver),
    path('admins_add_driver_post/',views.admins_add_driver_post),
    path('admins_add_driver_post/',views.admins_add_driver_post),
    path('admins_view_driver/',views.admins_view_driver),
    path('admins_view_driver_post/',views.admins_view_driver_post),
    path('admins_delete_driver/<id>',views.admins_delete_driver),
    path('admins_edit_driver/<id>',views.admins_edit_driver),
    path('admins_edit_driver_post/',views.admins_edit_driver_post),

    path('admins_view_complaints/',views.admins_view_complaints),
    path('admins_view_complaints_post/',views.admins_view_complaints_post),
    path('admins_sent_reply/<id>',views.admins_sent_reply),
    path('admins_sent_reply_post/',views.admins_sent_reply_post),



    path('admin_addvehicle/',views.admin_addvehicle),
    path('admin_addvehicle_post/',views.admin_addvehicle_post),

    path('admin_view_vehicle/',views.admin_view_vehicle),
    path('admin_view_vehicle_post/',views.admin_view_vehicle_post),
    path('admin_view_vehicle_post/',views.admin_view_vehicle_post),
    path('admin_delete_vehicles/<vid>',views.admin_delete_vehicles),
    path('admin_edit_vehicles/<id>',views.admin_edit_vehicles),
    path('admin_editvehicle_post/',views.admin_editvehicle_post),



    path('admin_change_password/',views.admin_change_password),
    path('admin_changepas_post/',views.admin_changepas_post),


    path('add_scategory/',views.add_scategory),
    path('add_scategory_post/',views.add_scategory_post),
    path('admin_view_servicecategory/',views.admin_view_servicecategory),
    path('admin_view_servicecategory_post/',views.admin_view_servicecategory_post),
    path('delete_category/<id>',views.delete_category),
    path('add_services/',views.add_services),
    path('add_services_post/',views.add_services_post),
    path('admin_view_service/',views.admin_view_service),
    path('admin_view_service_post/',views.admin_view_service_post),
    path('edit_services/<id>',views.edit_services),
    path('edit_services_post/',views.edit_services_post),
    path('delete_service/<id>',views.delete_service),
    path('admin_accept_request/<id>',views.admin_accept_request),
    path('admin_reject_request/<id>',views.admin_reject_request),
    path('admin_view_request/',views.admin_view_request),
    path('admin_view_request_post/',views.admin_view_request_post),
    path('admin_view_request_accepted/',views.admin_view_request_accepted),
    path('admin_view_request_post_accepted/',views.admin_view_request_post_accepted),


    path('driver_view_servicecategory/',views.driver_view_servicecategory),
    path('driver_view_request_status/',views.driver_view_request_status),
    path('driver_view_servicecategory_post/',views.driver_view_servicecategory_post),
    path('driver_view_service/<id>',views.driver_view_service),
    path('driver_sendrequest/',views.driver_sendrequest,name='driver_sendrequest'),
    path('admins_add_mechanic/',views.admins_add_mechanic),
    path('admins_add_mechanic_post/',views.admins_add_mechanic_post),
    path('admins_view_mechanic/',views.admins_view_mechanic),
    path('admins_view_mechanic_post/',views.admins_view_mechanic_post),
    path('admins_delete_mechanic/<id>',views.admins_delete_mechanic),
    path('admins_edit_mechanic/<id>',views.admins_edit_mechanic),
    path('admins_edit_mechanic_post/',views.admins_edit_mechanic_post),
    path('mhome/',views.mhome),
    path('admin_view_request_more/<oid>',views.admin_view_request_more),
    path('admin_view_request_approved/',views.admin_view_request_approved),
    path('admin_view_request_post_approved/',views.admin_view_request_post_approved),
    path('admin_view_request_more_approved/<id>',views.admin_view_request_more_approved),
    path('driver_view_request_approved/',views.driver_view_request_approved),
    path('driver_view_request_post_approved/',views.driver_view_request_post_approved),
    path('driver_view_request_more_approved/<oid>',views.driver_view_request_more_approved),




    path('admin_car_driver_assign/',views.admin_car_driver_assign),
    path('admin_car_driver_assign_post/',views.admin_car_driver_assign_post),
    path('admin_view_car_driver_assign/',views.admin_view_car_driver_assign),
    path('admin_delete_car_assign/<id>',views.admin_delete_car_assign),
    path('admin_view_car_driver_assign_post/',views.admin_view_car_driver_assign_post),
    path('admin_view_users/',views.admin_view_users),
    path('admin_view_users_post/',views.admin_view_users_post),







    path('driverhome/',views.driverhome),
    path('driver_view_profile/',views.driver_view_profile),
    path('driver_change_password/',views.driver_change_password),
    path('driver_view_booking_new/',views.driver_view_booking_new),
    path('driver_view_booking_new_post/',views.driver_view_booking_new_post),
    path('driver_picked/<id>',views.driver_picked),
    path('driver_cancelled/<id>',views.driver_cancelled),
    path('driver_dropped/',views.driver_dropped),
    path('driver_change_password/',views.driver_change_password),
    path('driver_changepas_post/',views.driver_changepas_post),
    path('addtocart/<sid>',views.addtocart),
    path('delete_cart/<id>',views.delete_cart),
    path('view_cart/',views.view_cart),



    path('uhome/',views.uhome),
    path('user_signup/',views.user_signup),
    path('user_signup_post/',views.user_signup_post),
    path('user_view_profile/',views.user_view_profile),
    path('user_edit_profile/',views.user_edit_profile),
    path('user_editprofile_post/',views.user_editprofile_post),
    path('user_add_complaint/',views.user_add_complaint),
    path('user_add_complaint_post/',views.user_add_complaint_post),
    path('user_view_complaint/',views.user_view_complaint),
    path('user_view_complaint_post/',views.user_view_complaint_post),
    path('user_view_cabs/',views.user_view_cabs),
    path('user_view_cabs_post/',views.user_view_cabs_post),
    path('user_booking/<vid>',views.user_booking),
    path('user_booking_post/',views.user_booking_post),

    path('user_change_password/', views.user_change_password),
    path('user_changepas_post/', views.user_changepas_post),
    path('user_view_booking/', views.user_view_booking),
    path('user_view_booking_post/', views.user_view_booking_post),
    path('user_cancelled/<id>', views.user_cancelled),

    path('forget_password/', views.forget_password),
    path('forget_password_post/', views.forget_password_post),

    path('sa/', views.sa),
    path('get_vehicles/', views.get_vehicles),
    path('userpayment/<bid>/<totalkm>', views.userpayment),
    path('userpayment_post/', views.userpayment_post),
    path('raz_pay/<amount>',views.raz_pay),


    ##############mechanic ###################



    path('generate_pdf_bill/<oid>',views.generate_pdf_bill),
    path('total_calculate/',views.total_calculate),
    path('mechanic_view_profile/',views.mechanic_view_profile),
    path('mechanic_view_request_approved/',views.mechanic_view_request_approved),
    path('mechanic_view_request_post_approved/',views.mechanic_view_request_post_approved),
    path('mechanic_view_request_more_approved/<oid>',views.mechanic_view_request_more_approved),
    path('mechanic_change_password/',views.mechanic_change_password),
    path('mechanic_changepas_post/',views.mechanic_changepas_post),

    ]

