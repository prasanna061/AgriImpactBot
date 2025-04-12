import gradio  as gr
import google.generativeai  as genai

# Gemini API configuration
genai.configure(api_key="AIzaSyABjjtDkWlJTGYgy5mkagHlDAEhpPTm1JI")

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Main function to generate the report
def generate_impact_report(farm_type, crop, location, energy_source, equipment):
    prompt = f"""
You are an environmental impact assessor for agricultural systems.

Given the following setup:
- Farm Type: {farm_type}
- Crop: {crop}
- Location: {location}
- Energy Source: {energy_source}
- Equipment Used: {equipment}

Analyze and generate a report covering:
1. Carbon Emissions
2. Water Usage
3. Soil Health Impact
4. Biodiversity Concerns
5. Suggested Improvements for Sustainability

Provide the analysis in a clear, structured, and user-friendly format.
    """
    response = model.generate_content(prompt)
    return response.text

# UI with Gradio Blocks
with gr.Blocks(theme=gr.themes.Default(primary_hue="green", secondary_hue="lime")) as demo:
    gr.Markdown("<h1 style='text-align: center;'>🌾 AgriImpactBot</h1>")
    gr.Markdown("<p style='text-align: center;'>Get a smart environmental impact report for your energy-powered farming setup 🌱</p>")

    with gr.Row():
        with gr.Column():
            farm_type = gr.Textbox(label="🏡 Farm Type", placeholder="e.g., Greenhouse, Open field")
            crop = gr.Textbox(label="🌾 Crop Type", placeholder="e.g., Tomatoes, Wheat")
            location = gr.Textbox(label="📍 Location", placeholder="e.g., Punjab, India")
        with gr.Column():
            energy_source = gr.Textbox(label="⚡ Energy Source", placeholder="e.g., Solar, Diesel")
            equipment = gr.Textbox(label="🛠️ Equipment Used", placeholder="e.g., Drip irrigation, Electric pump")

    generate_button = gr.Button("🚀 Generate Report")

    output = gr.Textbox(label="📄 Environmental Impact Report", lines=20, interactive=False)

    generate_button.click(
        fn=generate_impact_report,
        inputs=[farm_type, crop, location, energy_source, equipment],
        outputs=output
    )

demo.launch()
