
# Sample Diffusion ComfyUI extension

Allows the use of trained [dance diffusion/sample generator](https://github.com/Harmonai-org/sample-generator) models in ComfyUI.

## Installation
1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
2. Clone/download as zip and place ```SampleDiffusion``` folder in ```ComfyUI/custom_nodes```.
3. Move/copy playAudio.js from ```SampleDiffusion``` to ```ComfyUI/web/extensions```
4. Place models in ```ComfyUI/models/audio_diffusion``` ('audio_diffusion' entry in extra_model_paths.yaml is accepted).
5. Launch!
Includes a couple helper functions.

## Example

(Tip: right-click a node to convert an input to a pin you can connect to!)

![App Screenshot](https://i.imgur.com/cxNlYpU.png)

Feel free to check out my [other nodes](https://github.com/diontimmer/ComfyUI-Vextra-Nodes).

## Acknowledgements

 - [sample-diffusion](https://github.com/sudosilico/sample-diffusion)
 - [pythongosssss](https://github.com/pythongosssss) for the preview audio node & javascript magic.
 - [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
 - [Harmonai](https://github.com/Harmonai-org/sample-generator)
