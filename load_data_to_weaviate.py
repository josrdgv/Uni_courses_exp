import weaviate
from django.db import connection
from uni_app.models import (
    MergeCourse,
    CourseEra2,
    CourseCatalog,
    Coursera,
)

# Initialize Weaviate client
client = weaviate.Client("http://localhost:8080")  # Change URL if hosted remotely

# Function to create schema for a specific class
def create_schema(class_name, properties):
    schema = {
        "class": class_name,
        "properties": properties,
        "vectorizer": "none",  # Disable auto-vectorization
    }
    if not client.schema.contains({"class": class_name}):
        client.schema.create_class(schema)

# Function to upload data to Weaviate
def upload_data_to_weaviate(class_name, data):
    for obj in data:
        client.data_object.create(obj, class_name)
        print(f"Uploaded to class {class_name}: {obj['title']}")

# Add schema and upload data for each model
def load_data_into_weaviate():
    # MergeCourse schema and data
    create_schema(
        "MergeCourse",
        [
            {"name": "title", "dataType": ["text"]},
            {"name": "instructor", "dataType": ["text"]},
            {"name": "learning_obj", "dataType": ["text"]},
            {"name": "embedding", "dataType": ["number[]"]},
        ],
    )
    merge_course_data = [
        {
            "title": obj.title,
            "instructor": obj.instructor,
            "learning_obj": obj.learning_obj,
            "embedding": list(obj.embedding) if obj.embedding else None,
        }
        for obj in MergeCourse.objects.all()
    ]
    upload_data_to_weaviate("MergeCourse", merge_course_data)

    # CourseEra2 schema and data
    create_schema(
        "CourseEra2",
        [
            {"name": "Course_name", "dataType": ["text"]},
            {"name": "University", "dataType": ["text"]},
            {"name": "Difficulty_Level", "dataType": ["text"]},
            {"name": "embedding", "dataType": ["number[]"]},
        ],
    )
    course_era2_data = [
        {
            "Course_name": obj.Course_name,
            "University": obj.University,
            "Difficulty_Level": obj.Difficulty_Level,
            "embedding": list(obj.embedding) if obj.embedding else None,
        }
        for obj in CourseEra2.objects.all()
    ]
    upload_data_to_weaviate("CourseEra2", course_era2_data)

    # CourseCatalog schema and data
    create_schema(
        "CourseCatalog",
        [
            {"name": "Name", "dataType": ["text"]},
            {"name": "Description", "dataType": ["text"]},
            {"name": "Credit_Hours", "dataType": ["text"]},
            {"name": "embedding", "dataType": ["number[]"]},
        ],
    )
    course_catalog_data = [
        {
            "Name": obj.Name,
            "Description": obj.Description,
            "Credit_Hours": obj.Credit_Hours,
            "embedding": list(obj.embedding) if obj.embedding else None,
        }
        for obj in CourseCatalog.objects.all()
    ]
    upload_data_to_weaviate("CourseCatalog", course_catalog_data)

    # Coursera schema and data
    create_schema(
        "Coursera",
        [
            {"name": "title", "dataType": ["text"]},
            {"name": "skills", "dataType": ["text"]},
            {"name": "ratings", "dataType": ["number"]},
            {"name": "embedding", "dataType": ["number[]"]},
        ],
    )
    coursera_data = [
        {
            "title": obj.title,
            "skills": obj.skills,
            "ratings": float(obj.ratings) if obj.ratings else None,
            "embedding": list(obj.embedding) if obj.embedding else None,
        }
        for obj in Coursera.objects.all()
    ]
    upload_data_to_weaviate("Coursera", coursera_data)

# Call the function to load data
if __name__ == "__main__":
    load_data_into_weaviate()
