# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Certifications(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    certification_name = models.CharField()
    issuing_body = models.CharField()
    obtained_date = models.DateField()
    expiration_date = models.DateField()
    certification_number = models.CharField()
    maintenance_requirements = models.CharField(db_comment="CME hours, exams, etc.")
    document = models.ForeignKey("ProviderDocuments", models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "certifications"


class ContinuingEducation(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    activity_type = models.CharField(
        db_comment="conference, course, workshop, webinar, journal_review, research"
    )
    title = models.CharField()
    provider_organization = models.CharField(db_comment="who provided the education")
    credit_hours = models.DecimalField(
        max_digits=4, decimal_places=2, db_comment="CME/CE credits earned"
    )
    credit_type = models.CharField(db_comment="CME, CNE, CPE, etc.")
    completion_date = models.DateField()
    expiration_date = models.DateField(db_comment="if credits expire")
    category = models.CharField(db_comment="clinical, research, ethics, safety, etc.")
    specialty_relevant = models.CharField(db_comment="which specialty this applies to")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(db_comment="city/state or online")
    certificate_document = models.ForeignKey("ProviderDocuments", models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "continuing_education"


class DocumentAccessLog(models.Model):
    id = models.UUIDField(primary_key=True)
    provider_document = models.ForeignKey("ProviderDocuments", models.DO_NOTHING)
    accessed_by = models.UUIDField()
    access_type = models.CharField(db_comment="view, download, share")
    ip_address = models.CharField()
    user_agent = models.CharField()
    accessed_at = models.DateTimeField()
    reason = models.CharField()

    class Meta:
        db_table = "document_access_log"


class DocumentTypes(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True)
    description = models.CharField()
    is_required = models.BooleanField()
    validation_rules = models.CharField()
    category = models.CharField(
        db_comment="education, license, certification, experience, background, surgical"
    )
    created_at = models.DateTimeField()

    class Meta:
        db_table = "document_types"


class EncryptionKeys(models.Model):
    id = models.UUIDField(primary_key=True)
    key_identifier = models.CharField(unique=True)
    encrypted_key = models.CharField()
    algorithm = models.CharField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        db_table = "encryption_keys"


class MedicalEducation(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    education_type = models.CharField(
        db_comment="medical_school, residency, fellowship, internship"
    )
    institution_name = models.CharField()
    degree_type = models.CharField(db_comment="MD, DO, MBBS, etc.")
    specialty = models.CharField(db_comment="for residency/fellowship")
    start_date = models.DateField()
    graduation_date = models.DateField()
    honors_awards = models.CharField()
    thesis_research_title = models.CharField()
    supporting_document = models.ForeignKey("ProviderDocuments", models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "medical_education"


class Organizations(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    name = models.CharField()
    tax_id = models.CharField(unique=True)
    phone = models.CharField()
    address_line1 = models.CharField()
    address_line2 = models.CharField()
    city = models.CharField()
    website = models.CharField()
    org_type = models.CharField(db_comment="hospital, clinic, group_practice")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "organizations"


class ProviderDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    document_type = models.ForeignKey(DocumentTypes, models.DO_NOTHING)
    original_filename = models.CharField()
    file_data = models.BinaryField(
        db_comment="binary file content stored directly in database"
    )
    file_extension = models.CharField()
    file_size = models.BigIntegerField()
    mime_type = models.CharField()
    file_hash = models.CharField()
    expiration_date = models.DateField()
    status = models.CharField(db_comment="active, expired, pending_verification")
    uploaded_at = models.DateTimeField()
    verified_at = models.DateTimeField()
    verified_by = models.UUIDField()
    is_encrypted = models.BooleanField()
    encryption_key = models.ForeignKey(
        EncryptionKeys, models.DO_NOTHING, to_field="key_identifier"
    )

    class Meta:
        db_table = "provider_documents"


class ProviderDocumentsArchive(models.Model):
    id = models.UUIDField(primary_key=True)
    provider_id = models.UUIDField()
    document_type_id = models.UUIDField()
    original_filename = models.CharField()
    file_data = models.BinaryField()
    file_extension = models.CharField()
    file_size = models.BigIntegerField()
    mime_type = models.CharField()
    file_hash = models.CharField()
    expiration_date = models.DateField()
    status = models.CharField()
    uploaded_at = models.DateTimeField()
    verified_at = models.DateTimeField()
    verified_by = models.UUIDField()
    is_encrypted = models.BooleanField()
    encryption_key_id = models.CharField()

    class Meta:
        db_table = "provider_documents_archive"


class ProviderDocumentsDeleted(models.Model):
    id = models.UUIDField(primary_key=True)
    provider_id = models.UUIDField()
    document_type_id = models.UUIDField()
    original_filename = models.CharField()
    file_data = models.BinaryField()
    file_extension = models.CharField()
    file_size = models.BigIntegerField()
    mime_type = models.CharField()
    file_hash = models.CharField()
    expiration_date = models.DateField()
    status = models.CharField()
    uploaded_at = models.DateTimeField()
    verified_at = models.DateTimeField()
    verified_by = models.UUIDField()
    is_encrypted = models.BooleanField()
    encryption_key_id = models.CharField()

    class Meta:
        db_table = "provider_documents_deleted"


class ProviderExperiences(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    institution_name = models.CharField()
    department = models.CharField()
    position_title = models.CharField()
    experience_type = models.CharField(
        db_comment="clinical, research, administrative, teaching, volunteer"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_current_position = models.BooleanField()
    job_description = models.CharField()
    key_achievements = models.CharField()
    supervisor_name = models.CharField()
    supervisor_contact = models.CharField()
    hours_per_week = models.CharField()
    supporting_document = models.ForeignKey(ProviderDocuments, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "provider_experiences"


class ProviderLicenses(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    state_code = models.CharField(db_comment="US state code (CA, NY, TX, etc.)")
    state_name = models.CharField(db_comment="Full state name for clarity")
    license_number = models.CharField()
    license_type = models.CharField(db_comment="MD, DO, RN, PA, NP, etc.")
    specialty_category = models.CharField(
        db_comment="general, surgical, psychiatric, etc."
    )
    issued_date = models.DateField()
    expiration_date = models.DateField()
    renewal_date = models.DateField(db_comment="next required renewal date")
    status = models.CharField(db_comment="active, expired, suspended, revoked, pending")
    issuing_authority = models.CharField(db_comment="state medical board name")
    restrictions = models.CharField(db_comment="any limitations or conditions")
    document = models.ForeignKey(ProviderDocuments, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "provider_licenses"


class ProviderProfiles(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    organization = models.ForeignKey(Organizations, models.DO_NOTHING)
    profile_status = models.CharField(
        db_comment="pending_review, verified, rejected, expired"
    )
    created_at = models.DateTimeField()
    verified_at = models.DateTimeField()
    verified_by = models.UUIDField()
    expires_at = models.DateTimeField()
    verification_notes = models.CharField()
    is_public = models.BooleanField()
    profile_completeness = models.JSONField()

    class Meta:
        db_table = "provider_profiles"


class ProviderSpecialties(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey("Providers", models.DO_NOTHING)
    specialty_name = models.CharField()
    board_name = models.CharField()
    certified_date = models.DateField()
    expiration_date = models.DateField()
    certification_number = models.CharField()
    status = models.CharField(db_comment="active, expired, pending")
    requires_state_license = models.BooleanField(
        db_comment="indicates if specialty requires state-specific licensing"
    )
    created_at = models.DateTimeField()
    taxonomy = models.CharField()

    class Meta:
        db_table = "provider_specialties"


class Providers(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    first_name = models.CharField()
    last_name = models.CharField()
    npi_number = models.CharField(unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField()
    address = models.CharField()
    specialization = models.CharField()
    status = models.CharField(db_comment="active, inactive, pending")
    created_at = models.DateTimeField()
    most_recent_updated_at = models.DateTimeField()

    class Meta:
        db_table = "providers"


class SurgicalExperiences(models.Model):
    id = models.UUIDField(primary_key=True)
    provider = models.ForeignKey(Providers, models.DO_NOTHING)
    surgery_type = models.CharField(
        db_comment="orthopedic, cardiac, neurosurgery, general, etc.(the one in charge or attending"
    )
    procedure_name = models.CharField()
    institution_name = models.CharField()
    total_procedures = models.IntegerField()
    primary_surgeon_procedures = models.IntegerField(
        db_comment="procedures where provider was primary surgeon"
    )
    assistant_procedures = models.IntegerField(
        db_comment="procedures where provider was assistant"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    complexity_level = models.CharField(
        db_comment="basic, intermediate, advanced, expert"
    )
    complications_rate = models.DecimalField(
        max_digits=5, decimal_places=2, db_comment="percentage of complications"
    )
    patient_outcomes_notes = models.CharField()
    supporting_document = models.ForeignKey(ProviderDocuments, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    primary = models.BooleanField()
    attending = models.BooleanField()

    class Meta:
        db_table = "surgical_experiences"


class UserActionLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    action_type = models.CharField(max_length=50)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    record_id = models.IntegerField(blank=True, null=True)
    old_values = models.JSONField(blank=True, null=True)
    new_values = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    additional_context = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = "user_action_log"


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        extra_fields.setdefault("user_type", "User")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("user_type", "Admin")

        if extra_fields.get("user_type") != "Admin":
            raise ValueError("Superuser must have user_type='Admin'")

        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True)
    user_type = models.CharField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UsersManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    # is_staff and is_superuser are defaults for admin page.
    @property
    def is_staff(self):
        return self.user_type == "Admin"

    @property
    def is_superuser(self):
        return self.user_type == "Admin"

    def has_module_perms(self, app_label):
        return self.user_type == "Admin"

    def has_perm(self, perm, obj=None):
        return self.user_type == "Admin"


class IPBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.GenericIPAddressField(unique=True)
    failed_attempts = models.IntegerField(default=0)
    blocked_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "ip_block"
