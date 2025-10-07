CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "users" (
  "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  "email" varchar NOT NULL,
  "password_hash" BYTEA NOT NULL,
  "user_type" varchar NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT NOW(),
  "updated_at" timestamp NOT NULL DEFAULT NOW(),
  "is_active" boolean NOT NULL DEFAULT TRUE,
  "last_login" timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE "providers" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "first_name" varchar NOT NULL,
  "last_name" varchar NOT NULL,
  "npi_number" varchar UNIQUE NOT NULL,
  "date_of_birth" date NOT NULL,
  "phone" varchar NOT NULL,
  "address" varchar NOT NULL,
  "specialization" varchar NOT NULL,
  "status" varchar NOT NULL,
  "created_at" timestamp NOT NULL,
  "most_recent_updated_at" timestamp NOT NULL
);

CREATE TABLE "organizations" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid NOT NULL,
  "name" varchar NOT NULL,
  "tax_id" varchar UNIQUE NOT NULL,
  "phone" varchar NOT NULL,
  "address_line1" varchar NOT NULL,
  "address_line2" varchar NOT NULL,
  "city" varchar NOT NULL,
  "website" varchar NOT NULL,
  "org_type" varchar NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL
);

CREATE TABLE "provider_experiences" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "institution_name" varchar NOT NULL,
  "department" varchar NOT NULL,
  "position_title" varchar NOT NULL,
  "experience_type" varchar NOT NULL,
  "start_date" date NOT NULL,
  "end_date" date NOT NULL,
  "is_current_position" boolean NOT NULL,
  "job_description" varchar NOT NULL,
  "key_achievements" varchar NOT NULL,
  "supervisor_name" varchar NOT NULL,
  "supervisor_contact" varchar NOT NULL,
  "hours_per_week" varchar NOT NULL,
  "supporting_document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL
);

CREATE TABLE "surgical_experiences" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "surgery_type" varchar NOT NULL,
  "procedure_name" varchar NOT NULL,
  "institution_name" varchar NOT NULL,
  "total_procedures" integer NOT NULL,
  "primary_surgeon_procedures" integer NOT NULL,
  "assistant_procedures" integer NOT NULL,
  "start_date" date NOT NULL,
  "end_date" date NOT NULL,
  "complexity_level" varchar NOT NULL,
  "complications_rate" decimal(5,2) NOT NULL,
  "patient_outcomes_notes" varchar NOT NULL,
  "supporting_document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL,
  "primary" boolean NOT NULL,
  "attending" boolean NOT NULL
);

CREATE TABLE "document_types" (
  "id" uuid PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "description" varchar NOT NULL,
  "is_required" boolean NOT NULL,
  "validation_rules" varchar NOT NULL,
  "category" varchar NOT NULL,
  "created_at" timestamp NOT NULL
);

CREATE TABLE "provider_documents" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "document_type_id" uuid NOT NULL,
  "original_filename" varchar NOT NULL,
  "file_data" bytea NOT NULL,
  "file_extension" varchar NOT NULL,
  "file_size" bigint NOT NULL,
  "mime_type" varchar NOT NULL,
  "file_hash" varchar NOT NULL,
  "expiration_date" date NOT NULL,
  "status" varchar NOT NULL,
  "uploaded_at" timestamp NOT NULL,
  "verified_at" timestamp NOT NULL,
  "verified_by" uuid NOT NULL,
  "is_encrypted" boolean NOT NULL,
  "encryption_key_id" varchar NOT NULL
);


CREATE TABLE "provider_documents_archive" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "document_type_id" uuid NOT NULL,
  "original_filename" varchar NOT NULL,
  "file_data" bytea NOT NULL,
  "file_extension" varchar NOT NULL,
  "file_size" bigint NOT NULL,
  "mime_type" varchar NOT NULL,
  "file_hash" varchar NOT NULL,
  "expiration_date" date NOT NULL,
  "status" varchar NOT NULL,
  "uploaded_at" timestamp NOT NULL,
  "verified_at" timestamp NOT NULL,
  "verified_by" uuid NOT NULL,
  "is_encrypted" boolean NOT NULL,
  "encryption_key_id" varchar NOT NULL
);


CREATE TABLE "provider_documents_deleted" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "document_type_id" uuid NOT NULL,
  "original_filename" varchar NOT NULL,
  "file_data" bytea NOT NULL,
  "file_extension" varchar NOT NULL,
  "file_size" bigint NOT NULL,
  "mime_type" varchar NOT NULL,
  "file_hash" varchar NOT NULL,
  "expiration_date" date NOT NULL,
  "status" varchar NOT NULL,
  "uploaded_at" timestamp NOT NULL,
  "verified_at" timestamp NOT NULL,
  "verified_by" uuid NOT NULL,
  "is_encrypted" boolean NOT NULL,
  "encryption_key_id" varchar NOT NULL
);



CREATE TABLE "provider_specialties" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "specialty_name" varchar NOT NULL,
  "board_name" varchar NOT NULL,
  "certified_date" date NOT NULL,
  "expiration_date" date NOT NULL,
  "certification_number" varchar NOT NULL,
  "status" varchar NOT NULL,
  "requires_state_license" boolean NOT NULL,
  "created_at" timestamp NOT NULL,
  "taxonomy" varchar NOT NULL
);

CREATE TABLE "document_access_log" (
  "id" uuid PRIMARY KEY,
  "provider_document_id" uuid NOT NULL,
  "accessed_by" uuid NOT NULL,
  "access_type" varchar NOT NULL,
  "ip_address" varchar NOT NULL,
  "user_agent" varchar NOT NULL,
  "accessed_at" timestamp NOT NULL,
  "reason" varchar NOT NULL
);

CREATE TABLE "provider_licenses" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "state_code" varchar NOT NULL,
  "state_name" varchar NOT NULL,
  "license_number" varchar NOT NULL,
  "license_type" varchar NOT NULL,
  "specialty_category" varchar NOT NULL,
  "issued_date" date NOT NULL,
  "expiration_date" date NOT NULL,
  "renewal_date" date NOT NULL,
  "status" varchar NOT NULL,
  "issuing_authority" varchar NOT NULL,
  "restrictions" varchar NOT NULL,
  "document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL
);

CREATE TABLE "certifications" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "certification_name" varchar NOT NULL,
  "issuing_body" varchar NOT NULL,
  "obtained_date" date NOT NULL,
  "expiration_date" date NOT NULL,
  "certification_number" varchar NOT NULL,
  "maintenance_requirements" varchar NOT NULL,
  "document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL
);

CREATE TABLE "medical_education" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "education_type" varchar NOT NULL,
  "institution_name" varchar NOT NULL,
  "degree_type" varchar NOT NULL,
  "specialty" varchar NOT NULL,
  "start_date" date NOT NULL,
  "graduation_date" date NOT NULL,
  "honors_awards" varchar NOT NULL,
  "thesis_research_title" varchar NOT NULL,
  "supporting_document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL
);

CREATE TABLE "continuing_education" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "activity_type" varchar NOT NULL,
  "title" varchar NOT NULL,
  "provider_organization" varchar NOT NULL,
  "credit_hours" decimal(4,2) NOT NULL,
  "credit_type" varchar NOT NULL,
  "completion_date" date NOT NULL,
  "expiration_date" date NOT NULL,
  "category" varchar NOT NULL,
  "specialty_relevant" varchar NOT NULL,
  "cost" decimal(10,2) NOT NULL,
  "location" varchar NOT NULL,
  "certificate_document_id" uuid NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp NOT NULL
);

CREATE TABLE "provider_profiles" (
  "id" uuid PRIMARY KEY,
  "provider_id" uuid NOT NULL,
  "organization_id" uuid NOT NULL,
  "profile_status" varchar NOT NULL,
  "created_at" timestamp NOT NULL,
  "verified_at" timestamp NOT NULL,
  "verified_by" uuid NOT NULL,
  "expires_at" timestamp NOT NULL,
  "verification_notes" varchar NOT NULL,
  "is_public" boolean NOT NULL,
  "profile_completeness" jsonb NOT NULL
);

CREATE TABLE "encryption_keys" (
  "id" uuid PRIMARY KEY,
  "key_identifier" varchar UNIQUE NOT NULL,
  "encrypted_key" varchar NOT NULL,
  "algorithm" varchar NOT NULL,
  "created_at" timestamp NOT NULL,
  "is_active" boolean NOT NULL
);

CREATE TABLE user_action_log (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    action_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(100),
    record_id INTEGER,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    user_agent varchar,
    session_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    additional_context JSONB
);

-- Add indexes for common queries
CREATE INDEX idx_user_action_log_user_id ON user_action_log(user_id);
CREATE INDEX idx_user_action_log_created_at ON user_action_log(created_at);
CREATE INDEX idx_user_action_log_action_type ON user_action_log(action_type);
CREATE INDEX idx_user_action_log_table_record ON user_action_log(table_name, record_id);

CREATE OR REPLACE FUNCTION log_user_action()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_action_log (
        user_id, action_type, table_name, record_id,
        old_values, new_values, created_at
    ) VALUES (
        COALESCE(current_setting('app.user_id', true)::INTEGER, 0),
        TG_OP,
        TG_TABLE_NAME,
        COALESCE(NEW.id, OLD.id),
        CASE WHEN TG_OP = 'DELETE' THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) ELSE NULL END,
        NOW()
    );
    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

COMMENT ON COLUMN "users"."user_type" IS 'provider, organization, admin';

COMMENT ON COLUMN "providers"."status" IS 'active, inactive, pending';

COMMENT ON COLUMN "organizations"."org_type" IS 'hospital, clinic, group_practice';

COMMENT ON COLUMN "provider_experiences"."experience_type" IS 'clinical, research, administrative, teaching, volunteer';

COMMENT ON COLUMN "surgical_experiences"."surgery_type" IS 'orthopedic, cardiac, neurosurgery, general, etc.(the one in charge or attending';

COMMENT ON COLUMN "surgical_experiences"."primary_surgeon_procedures" IS 'procedures where provider was primary surgeon';

COMMENT ON COLUMN "surgical_experiences"."assistant_procedures" IS 'procedures where provider was assistant';

COMMENT ON COLUMN "surgical_experiences"."complexity_level" IS 'basic, intermediate, advanced, expert';

COMMENT ON COLUMN "surgical_experiences"."complications_rate" IS 'percentage of complications';

COMMENT ON COLUMN "document_types"."category" IS 'education, license, certification, experience, background, surgical';

COMMENT ON COLUMN "provider_documents"."file_data" IS 'binary file content stored directly in database';

COMMENT ON COLUMN "provider_documents"."status" IS 'active, expired, pending_verification';

COMMENT ON COLUMN "provider_specialties"."status" IS 'active, expired, pending';

COMMENT ON COLUMN "provider_specialties"."requires_state_license" IS 'indicates if specialty requires state-specific licensing';

COMMENT ON COLUMN "document_access_log"."access_type" IS 'view, download, share';

COMMENT ON COLUMN "provider_licenses"."state_code" IS 'US state code (CA, NY, TX, etc.)';

COMMENT ON COLUMN "provider_licenses"."state_name" IS 'Full state name for clarity';

COMMENT ON COLUMN "provider_licenses"."license_type" IS 'MD, DO, RN, PA, NP, etc.';

COMMENT ON COLUMN "provider_licenses"."specialty_category" IS 'general, surgical, psychiatric, etc.';

COMMENT ON COLUMN "provider_licenses"."renewal_date" IS 'next required renewal date';

COMMENT ON COLUMN "provider_licenses"."status" IS 'active, expired, suspended, revoked, pending';

COMMENT ON COLUMN "provider_licenses"."issuing_authority" IS 'state medical board name';

COMMENT ON COLUMN "provider_licenses"."restrictions" IS 'any limitations or conditions';

COMMENT ON COLUMN "certifications"."maintenance_requirements" IS 'CME hours, exams, etc.';

COMMENT ON COLUMN "medical_education"."education_type" IS 'medical_school, residency, fellowship, internship';

COMMENT ON COLUMN "medical_education"."degree_type" IS 'MD, DO, MBBS, etc.';

COMMENT ON COLUMN "medical_education"."specialty" IS 'for residency/fellowship';

COMMENT ON COLUMN "continuing_education"."activity_type" IS 'conference, course, workshop, webinar, journal_review, research';

COMMENT ON COLUMN "continuing_education"."provider_organization" IS 'who provided the education';

COMMENT ON COLUMN "continuing_education"."credit_hours" IS 'CME/CE credits earned';

COMMENT ON COLUMN "continuing_education"."credit_type" IS 'CME, CNE, CPE, etc.';

COMMENT ON COLUMN "continuing_education"."expiration_date" IS 'if credits expire';

COMMENT ON COLUMN "continuing_education"."category" IS 'clinical, research, ethics, safety, etc.';

COMMENT ON COLUMN "continuing_education"."specialty_relevant" IS 'which specialty this applies to';

COMMENT ON COLUMN "continuing_education"."location" IS 'city/state or online';

COMMENT ON COLUMN "provider_profiles"."profile_status" IS 'pending_review, verified, rejected, expired';

ALTER TABLE "providers" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "organizations" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "provider_profiles" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "provider_profiles" ADD FOREIGN KEY ("organization_id") REFERENCES "organizations" ("id");

ALTER TABLE "provider_profiles" ADD FOREIGN KEY ("verified_by") REFERENCES "users" ("id");

ALTER TABLE "provider_documents" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "provider_documents" ADD FOREIGN KEY ("document_type_id") REFERENCES "document_types" ("id");

ALTER TABLE "provider_documents" ADD FOREIGN KEY ("verified_by") REFERENCES "users" ("id");

ALTER TABLE "provider_documents" ADD FOREIGN KEY ("encryption_key_id") REFERENCES "encryption_keys" ("key_identifier");

ALTER TABLE "document_access_log" ADD FOREIGN KEY ("provider_document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "document_access_log" ADD FOREIGN KEY ("accessed_by") REFERENCES "users" ("id");

ALTER TABLE "provider_licenses" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "provider_licenses" ADD FOREIGN KEY ("document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "certifications" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "certifications" ADD FOREIGN KEY ("document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "provider_specialties" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "provider_experiences" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "provider_experiences" ADD FOREIGN KEY ("supporting_document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "surgical_experiences" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "surgical_experiences" ADD FOREIGN KEY ("supporting_document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "medical_education" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "medical_education" ADD FOREIGN KEY ("supporting_document_id") REFERENCES "provider_documents" ("id");

ALTER TABLE "continuing_education" ADD FOREIGN KEY ("provider_id") REFERENCES "providers" ("id");

ALTER TABLE "continuing_education" ADD FOREIGN KEY ("certificate_document_id") REFERENCES "provider_documents" ("id");
