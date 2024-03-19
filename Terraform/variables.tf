locals {
  current_time = formatdate("YYYYMMDDhhmmss", timestamp())
}

variable "BQ_Dataset" {
  description = "The name of the BigQuery table the data will be written to."
  default     = "zomato"
  type        = string
}

variable "Region" {
  description = "The location where the resources should be created."
  default     = "asia-south1"
  type        = string
}

variable "Project_ID" {
  description = "Project ID of the project"
  default     = "zomato-zoomcamp"
  type        = string
}

variable "Storage_class" {
  description = "The storage class for the bucket to be created."
  default     = "STANDARD"
  type        = string
}

variable "Public_Acess" {
  description = "Public access to be inherited or enforced"
  default     = "enforced"
  type        = string
}

