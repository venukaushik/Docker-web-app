from flask import Flask

app = Flask(__name__)

# Define a consistent color palette
primary_color = "#007bff"
primary_darker = "#0056b3"
secondary_color = "#6c757d"
light_bg = "#f8f9fa"
dark_text = "#333"
medium_text = "#555"
border_color = "#dee2e6"

# Define a nice font stack
body_font = "Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
heading_font = body_font

base_style = f"""
    body {{
        font-family: {body_font};
        background-color: {light_bg};
        color: {dark_text};
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        margin: 0;
        padding: 20px; /* Add some padding to the body */
        box-sizing: border-box; /* Ensure padding doesn't affect width */
    }}
    .container {{
        background-color: #fff;
        padding: 40px;
        border-radius: 12px;           
