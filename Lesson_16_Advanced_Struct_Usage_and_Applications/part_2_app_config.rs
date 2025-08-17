#[derive(Debug)]
struct AppConfig {
    db_url: String,
    api_key: String,
    timeout: Option<u32>, // Optional field
}

fn main() {
    let config = AppConfig {
        db_url: "localhost:5432".to_string(),
        api_key: "supersecretapikey".to_string(),
        timeout: None, // No timeout specified
    };

    println!("{:?}", config);
}
