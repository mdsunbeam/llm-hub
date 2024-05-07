<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mdsunbeam/llm-hub">
    <img src="images/llm-hub-logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Large Language Model Hub</h3>

  <p align="center">
    Easily start your project with the frontier models of OpenAI, Anthropic, and Google.
    <br />
    <a href="https://github.com/mdsunbeam/llm-hub"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mdsunbeam/llm-hub">View Demo</a>
    ·
    <a href="https://github.com/mdsunbeam/llm-hub/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/mdsunbeam/llm-hub/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

Repository that allows you to use the popular LLMs through their APIs or locally. The first version will have GPT models from OpenAI, Claude 3 models from Anthropic, Gemini models from Google, and Llama 3 models from Meta AI.

The emphasis is on simplicity and ease of use for these frontier models. It should be intuitive on how to send inputs to the model and manage the dialogue history.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The first thing to set up is your OpenAI, Anthropic, and Google API keys. You need OpenAI for the GPT models, Anthropic for the Claude 3 models, and Google for the Gemini models.

### Prerequisites

1. Get an API key for OpenAI at: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Get directions for how to generate an API key for Anthropic at: [https://docs.anthropic.com/claude/reference/getting-started-with-the-api](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
3. Get an API key for Google at: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Next, create three text files called `OPENAI_API_KEY.txt`, `ANTHROPIC_API_KEY.txt`, `GOOGLE_API_KEY.txt`. Paste your respective API keys into the text files.

### Installation

1. Make Python virtual environment
   ```sh
   python3.10 -m venv llm-hub-env
   source llm-hub-env/bin/activate
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/mdsunbeam/llm-hub.git
   cd llm-hub
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Handling of image and text with all frontier models
- [ ] Llama 3
- [ ] Pass arbitrary amount of messages in one go
- [ ] Poll all frontier models for the same prompt
- [ ] Reproduce results on popular LLM and multimodal datasets 

See the [open issues](https://github.com/mdsunbeam/llm-hub/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[@MdSunbeam](https://twitter.com/MdSunbeam) - mdsunbeam3.14@gmail.com

Project Link: [https://github.com/mdsunbeam/llm-hub](https://github.com/mdsunbeam/llm-hub)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mdsunbeam/llm-hub.svg?style=for-the-badge
[contributors-url]: https://github.com/mdsunbeam/llm-hub/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mdsunbeam/llm-hub.svg?style=for-the-badge
[forks-url]: https://github.com/mdsunbeam/llm-hub/network/members
[stars-shield]: https://img.shields.io/github/stars/mdsunbeam/llm-hub.svg?style=for-the-badge
[stars-url]: https://github.com/mdsunbeam/llm-hub/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mdsunbeam
[product-screenshot]: images/screenshot.png
