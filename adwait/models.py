
from django.db import models


class AdwaitappAboutAdwait(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_about_adwait'


class AdwaitappBlogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    dept_id_id = models.BigIntegerField()
    main_service_id_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_blogs'


class AdwaitappContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_contact'


class AdwaitappCustomers(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    business = models.SmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    more_info = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_customers'


class AdwaitappIndustries(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'adwaitapp_industries'


class AdwaitappInquiries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    dept_id_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_inquiries'


class AdwaitappMainServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    dept_id_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_main_services'


class AdwaitappSubServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    main_service_id_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_sub_services'


class AdwaitappTestimonials(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)
    customer_id_id = models.BigIntegerField()
    dept_id_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_testimonials'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
