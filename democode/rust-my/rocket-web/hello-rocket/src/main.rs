use rocket::{delete, get, post, put, routes};

/// GET  http://127.0.0.1:8000/
#[get("/")]
async fn index() -> String {
    "Hello, rocket!".to_string()
}

/// GET  http://127.0.0.1:8000/user/list
#[get("/list")]
async fn user_list() -> String {
    "List of users".to_string()
}

/// GET  http://127.0.0.1:8000/user/info/123
#[get("/info/<_id>")]
async fn user_info(_id: usize) -> String {
    "User info".to_string()
}

/// POST  http://127.0.0.1:8000/user/add
#[post("/add")]
async fn add_user() -> String {
    "User added".to_string()
}

/// PUT  http://127.0.0.1:8000/user/update/123
#[put("/update/<_id>")]
async fn update_user(_id: usize) -> String {
    "User updated".to_string()
}

/// DELETE  http://127.0.0.1:8000/user/delete/123
#[delete("/delete/<_id>")]
async fn delete_user(_id: i32) -> String {
    "User deleted".to_string()
}


#[rocket::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    rocket::build()
        .mount("/", routes![index])
        .mount("/user", routes![user_list,user_info, add_user, update_user, delete_user])
        .launch().await?;
    Ok(())
}