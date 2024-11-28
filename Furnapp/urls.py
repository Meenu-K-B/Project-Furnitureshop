from django.urls import path
from Furnapp import views
urlpatterns = [
    path('index_page/',views.indexpage,name="index_page"),
    path('Add_cat/',views.AddCategory,name="Add_cat"),
    path('Save_Category/',views.Save_Category,name="Save_Category"),
    path('Display_Category/',views.display_Categories,name="Display_Category"),
    path('Edit_Cat/<int:cat_id>/',views.EditCategories,name="Edit_Cat"),
    path('Update_Cat/<int:cat_id>/',views.Update_Category,name="Update_Cat"),
    path('Add_Product/',views.Addproduct,name="Add_Product"),
    path('Save_Product/',views.Save_Product,name="Save_Product"),
    path('Display_Pro/',views.display_Product,name="Display_Pro"),
    path('Edit_Pro/<int:dat_id>/',views.EditProduct,name="Edit_Pro"),
    path('Delete_Pro/<int:Pro_id>/',views.DeleteProduct,name="Delete_Pro"),
    path('Update_Pro/<int:P_id>/',views.Update_Product,name="Update_Pro"),
    path('Delete_Cat/<int:C_id>/',views.DeleteCat,name="Delete_Cat"),
    path('admin_login/',views.login_page,name="admin_login"),
    path('admin_loginpage/',views.admin_login,name="admin_loginpage"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('Contact_Details/',views.display_Contact,name="Contact_Details"),
    path('Contact_Delete/<int:Con_id>/',views.DeleteContact,name="Contact_Delete")






]