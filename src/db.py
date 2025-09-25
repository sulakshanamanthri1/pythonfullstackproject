# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load environmental variables
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)

#create task
def create_user(username,email,password):
    return supabase.table("users").insert({
        "username":username,
        "email":email,
        "password":password,
    }).execute()
#Get ALL users
def get_all_users():
    return supabase.table("users").select("*").execute()

# tasks table
def create_task(user_id,description,completed,created_at,updated_at):
    return supabase.table("tasks").insert({
        "user_id":user_id,
        "description":description,
        "created_at":created_at,
        "completed":completed,
        "updated_at":updated_at
    }).execute()
def get_all_tasks():
    return supabase.table("tasks").select("*").order("created_at").execute()

def update_task(task_id, completed):
    return supabase.table("tasks").update({"completed": completed}).eq("id", task_id).execute()

def delete_tasks(user_id):
    return supabase.table("tasks").delete().eq("id",user_id).execute()
