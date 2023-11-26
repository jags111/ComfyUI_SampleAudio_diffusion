# ComfyUI_SampleAudio_diffusion
# Sample Diffusion ComfyUI extension (modified)<br>
🌈 🍬 Note we have made changes to the original repo here and adding new nodes to experiment and certain features may be experimental and may need contant updates. If you face any issue, ensure you have updated ComfyUi to the latest version and updates all requirements and share your workflow in the Issues. we are thankful to Harmonai-org and origianl repo for same🌈 <br>

## Features
Allows the use of trained [dance diffusion/sample generator](https://github.com/Harmonai-org/sample-generator) models in ComfyUI.<br>
Also included are two optional extensions of the extension (lol); Wave Generator for creating primitive waves aswell as a wrapper for the Pedalboard library.<br>
The pedalboard wrapper allows us to wrap most vst3s and control them, for now only a wrapper for OTT is included. Any suggestions are welcome.<br>
Includes a couple helper functions.

## Installation
1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
2. Use 'ComfyManager' to install the node and update everything as required. Ensure the comfyUI is the latest version.
3. Clone/download as zip and place ```ComfyUI_SampleAudio_diffusion``` folder in ```ComfyUI/custom_nodes```.
4. Move/copy playAudio.js from ```SampleDiffusion``` to ```ComfyUI/web/extensions```
5. Place models in ```ComfyUI/models/audio_diffusion``` ('model_folder' entry in config.yaml is accepted).<br>
4.1 (Optional) Install [xfer OTT VST3](https://xferrecords.com/freeware)
6. Launch!

## Example

(Tip: right-click a node to convert an input to a pin you can connect to!)

![App Screenshot](https://i.imgur.com/cxNlYpU.png)

Feel free to check out my [other nodes](https://github.com/diontimmer/ComfyUI-Vextra-Nodes).

## Acknowledgements

 - [sample-diffusion](https://github.com/sudosilico/sample-diffusion)
 - [pythongosssss](https://github.com/pythongosssss) for the preview audio node & javascript magic.
 - [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
 - [Harmonai](https://github.com/Harmonai-org/sample-generator)
 - [pedalboard](https://github.com/spotify/pedalboard)
 - [xfer OTT](https://xferrecords.com/freeware)
