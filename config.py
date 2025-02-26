conf = {
    "error_info":           "سرور شلوغ است لطفا صبور باشید",
    "before_generate_info": "🤖Fibonacci AI Generating🤖",
    "download_pic_notify":  "🤖Loading picture🤖",
    "model_1":              "fibonacci-1.5-flash-exp",
    "model_2":              "fibonacci-1-pro-latest",
    "n": 30  #Number of historical records to keep
}



generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1024,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {   
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]
