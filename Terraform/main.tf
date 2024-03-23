terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.18.0"
    }
  }
}

provider "google" {
  project     = var.Project_ID
  region      = var.Region
}


resource "google_storage_bucket" "zomato-bucket" {
  name          = "zomato_bucket_${local.current_time}"
  location      = var.Region
  storage_class = var.Storage_class
  force_destroy = true
  public_access_prevention = var.Public_Acess
  versioning {
    enabled = "true"
  }
}


resource "google_bigquery_dataset" "zomato-dataset-bq" {
  dataset_id = var.BQ_Dataset
  project = var.Project_ID
  location = var.Region
}
