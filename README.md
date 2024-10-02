# FlowMinds

FlowMinds is an AI-powered application that generates detailed explanations and visual flowcharts for complex processes and concepts. By leveraging the power of OpenAI's GPT model and Mermaid flowchart syntax, FlowMinds transforms natural language inputs into comprehensive textual descriptions and corresponding visual representations.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Use Cases](#use-cases)
- [Technical Details](#technical-details)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Natural Language Input**: Describe any process or concept in plain English.
- **AI-Generated Explanations**: Utilizes OpenAI's GPT model for detailed, informative responses.
- **Automated Flowchart Creation**: Transforms AI-generated explanations into structured Mermaid flowcharts.
- **Complex Process Handling**: Represents intricate workflows with up to 15-20 nodes.
- **Visual Differentiation**: Uses various node shapes and colors to distinguish between different types of steps or processes.
- **Subprocess Representation**: Employs subgraphs to group related processes, allowing for hierarchical representation.
- **Interactive User Interface**: Built with Streamlit for a user-friendly, responsive web experience.
- **Real-time Generation**: Provides instant results, with both explanation and flowchart generated on-demand.

## How It Works

1. **User Input**: Enter a question or describe a process in the text input field.
2. **AI Response Generation**: The app sends the user's input to OpenAI's API, generating a detailed explanation.
3. **Flowchart Creation**: Another API call transforms the explanation into a Mermaid flowchart, following specified guidelines for complex process representation.
4. **Result Display**: The app presents both the textual explanation and the Mermaid flowchart code.
5. **Visualization Instructions**: Clear steps are provided for users to visualize the flowchart using an external Mermaid live editor.

## Installation

To set up FlowMinds locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/FlowMinds.git
   cd FlowMinds
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To run FlowMinds:

1. Ensure your virtual environment is activated.
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).
4. Enter your question or describe a process in the input field and click "Generate Response and Flowchart".
5. View the generated explanation and Mermaid flowchart code.
6. To visualize the flowchart, copy the Mermaid code and paste it into [Mermaid Live Editor](https://mermaid.live/).

## Use Cases

- **Educational Tool**: Visualize complex academic concepts or scientific processes.
- **Business Process Modeling**: Map out intricate business workflows or decision trees.
- **Project Planning**: Create visual representations of project lifecycles or methodologies.
- **Technical Documentation**: Generate flowcharts for software architectures or system designs.
- **Problem-Solving**: Break down complex problems into visual, step-by-step processes.

## Technical Details

- **Frontend**: Streamlit (Python-based web application framework)
- **Backend**: Python
- **AI Model**: OpenAI's GPT-3.5-turbo
- **Flowchart Syntax**: Mermaid (JavaScript-based diagramming and charting tool)
- **Environment Management**: dotenv for secure API key handling

## Limitations

- Flowchart complexity is limited to 15-20 nodes for clarity and rendering feasibility.
- Very intricate processes may require manual adjustments or multiple flowcharts.
- The quality of the flowchart depends on the clarity and specificity of the user's input.
- Visualization requires an external tool (Mermaid live editor) for rendering the flowchart.

## Contributing

Contributions to FlowMinds are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
