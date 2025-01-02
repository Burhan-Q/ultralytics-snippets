# Ultralytics Snippets for Visual Studio Code

<div align="center">
  <p>
    <a href="https://github.com/ultralytics/assets/releases/tag/v8.2.0" target="_blank">
      <img width="80%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="YOLO Vision banner"></a>
  </p>
</div>

A [Python snippets extension for VS Code](https://marketplace.visualstudio.com/items?itemName=Ultralytics.ultralytics-snippets) to assist with development using the [Ultralytics package](https://github.com/ultralytics/ultralytics). These snippets will help you code with Ultralytics faster and help provide some boilerplate examples to test out. Open an Issue or a Pull Request to have your snippet added! 🚀 Also works with [`neovim`](#use-with-neovim)!

<div align="center">
  <p>
    <img src="https://github.com/Burhan-Q/ultralytics-snippets/assets/62214284/42ad0b17-e752-479c-9c6c-e451fffbe8b3" alt="Snippet Prediction Preview">
    <strong>NOTE:</strong> Tab-completion used to complete snippet and quickly hop into fields.
  </p>
</div>

## Updates

- 2025-01-02 :: Updated KWARGs snippets to include more drop down options, added drop downs for all boolean args, add missing args, update some defaults
- 2024-10-03 :: [Ultralytics YOLO11](https://docs.ultralytics.com/models/yolo11) added! YOLO11 will now be the default model.
- 2024-08-26 :: Ultralytics VS Code Snippets integration [documentation page](https://docs.ultralytics.com/integrations/vscode).
- 2024-08-14 :: Extension size is now ~100x smaller.
- 2024-08-03 :: Tracking example and KWARGs snippets added.
- 2024-07-30 :: SAM2 examples included.
- 2024-07-24 :: Lots of new snippets and updates.
- 2024-07-17 :: Adds YOLO-world snippet with custom prompts, updates reference links, and adds keyword argument.
- 2024-07-12 :: Model export snippet added and adds keyword argument.

## Installation

<img alt="Visual Studio Code Icon" src="https://code.visualstudio.com/assets/images/code-stable.png" width="20" height="20"> <a href="https://marketplace.visualstudio.com/items?itemName=Ultralytics.ultralytics-snippets"><img alt="Visual Studio Marketplace Installs" src="https://img.shields.io/visual-studio-marketplace/i/Ultralytics.ultralytics-snippets?label=Marketplace%20Downloads&color=blue"></a>

### From the Web

#### Method-1

1. Visit the VS Code Extension Marketplace by going to https://marketplace.visualstudio.com/VSCode and search for `Ultralytics-Snippets`.

#### Method-2

1. Follow [this link](https://marketplace.visualstudio.com/items?itemName=Ultralytics.ultralytics-snippets) to visit the extension page directly.

2. Click the "Install" button and allow your browser to launch a VS Code session.

    ![VS Code marketplace extension install](https://github.com/user-attachments/assets/b40cc8e2-2353-4165-859a-c84eec070db6)

### From VS Code

1. Navigate to the Extensions menu, and search for `Ultralytics-Snippets`.

2. Click the "Install" button.

    ![VS Code extension menu](https://github.com/user-attachments/assets/9de46d22-ef7b-4765-ba2c-d0459cafa4dc)

### From the CLI

You can also install the latest version of the `Ultralytics-Snippets` VS Code extension using the following command.

```sh
code --install-extension ultralytics.ultralytics-snippets
```

## Snippets Syntax

All snippets use the format:

<p style="text-indent:13px;">
<code>{PREFIX}.{ROOT}*-{DESCRIPTOR}</code>
</p>

- `{PREFIX}` is always `ultra`

- `{ROOT}` denotes a common "root" verb or noun such as `import` or `results`. There will always be _at least one_ root common with other snippets, but it's possible there could be more than one, such as `result-boxes`.

- `{DESCRIPTOR}` will be related to the snippet functionality and all words will be separated with hyphens `-` the snippet alias.

## Import

Import snippets are for common objects that would be imported from the Ultralytics library. 

| Alias                       | Description                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| `ultra.import-model`        | Add line to import Ultralytics YOLO                                                          |
| `ultra.import-assets`       | Import Ultralytics ASSETS directory constant.                                                |
| `ultra.import-results`      | Import Ultralytics Results class (usually for type hinting).                                 |
| `ultra.import-annotator`    | Import Ultralytics auto_annotate function.                                                   |
| `ultra.import-coco2yolo`    | Import Ultralytics function to convert annotations from COCO to YOLO format.                 |
| `ultra.import-bbox2seg`     | Import Ultralytics function to convert horizontal bounding boxes to segmentation contours.   |
| `ultra.import-seg2bbox`     | Import Ultralytics function to convert segmentation contours into horizontal bounding boxes. |
| `ultra.import-box-convert`  | Import Ultralytics function for converting bounding box coordinates.                         |
| `ultra.import-formats`      | Import Ultralytics supported file formats constant.                                          |
| `ultra.import-task-result`  | Import task-based results class (generally helpful for type hinting).                        |

### Snippet Example

<details><summary><code>ultra.import-model</code> Snippet</summary>
<p>

Drop-down select available for `Model` class to import.

```py
Model = "YOLO"
from ultraltyics import f"{Model}"  # not intended to represent valid code
```

</p></details>

## Results

These snippets will provide shortcuts for working with `ultralytics.engine.results.Results` objects returned from model inference. See the [Working with Results][pred results] of the documentation and the [Results class] reference page for more information.

| Alias                        | Description                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `ultra.result-class-str`     | Convert class indices to class string names for a single image result.                                             |
| `ultra.result-data`          | Get result data array of detections from a single image result.                                                    |
| `ultra.result-loop`          | Iterate prediction results from an Ultralytics model.                                                              |
| `ultra.result-box-xyxy`      | Get pixel-value `(x1, y1, x2, y2)` bounding box coordinates from a single image result.                            |
| `ultra.result-box-xywh`      | Get pixel-value `(x-center, y-center, w, h)` bounding box coordinates from a single image result.                  |
| `ultra.result-mask-binary`   | Get binary segmentation masks from a single image result. NOTE: `[N, H, W]` shape, with inference H, W dimensions. |
| `ultra.result-mask-contours` | Get segmentation contours with pixel value `xy` or normalized `xyn` coordinates.                                   |
| `ultra.result-obb-xywhr`     | Get OBB rotated bounding boxes in pixel value `[x, y, w, h, r]` coordinates as torch.Tensor array.                 |
| `ultra.result-orig-image`    | Get original image from a single image result.                                                                     |
| `ultra.result-filter-class`  | Filter prediction results by class ID. Using `classes` keyword argument for prediction should be preferred.        |

### Snippet Example

<details><summary><code>ultra.result-loop</code> Snippet</summary>
<p>

```py
for result in results:
    result.boxes.data  # torch.Tensor array
```

**NOTE:** `results` is a placeholder and can be modified to match existing naming schema.

</p></details>

## Models

Shortcuts for initializing pretrained [Ultralytics models][models], like [YOLOv8].

| Alias                    | Description                                                  | Reference                                             |
| ------------------------ | ------------------------------------------------------------ | ----------------------------------------------------- |
| `ultra.yolo-model`       | Shortcut to initialize YOLO model.                           | [YOLOv5], [YOLOv8], [YOLOv9], [YOLOv10], [YOLO-World] |
| `ultra.yolo-export`      | Shortcut to export YOLO model weights.                       | [Model Export]                                        |
| `ultra.sam-model`        | Shortcut to initialize SAM.                                  | [SAM]                                                 |
| `ultra.mobileam-model`   | Shortcut to initialize MobileSAM.                            | [Mobile SAM]                                          |
| `ultra.fastam-model`     | Shortcut to initialize FastSAM.                              | [FastSAM]                                             |
| `ultra.nas-model`        | Shortcut to initialize YOLO-NAS model.                       | [YOLO-NAS]                                            |
| `ultra.rtdetr-model`     | Shortcut to initialize RTDETR model.                         | [RTDETR]                                              |
| `ultra.yolo-world-model` | Shortcut to initialize YOLO-world model, with class prompts. | [YOLO-World]                                          |
| `ultra.sam2-bboxes`      | Shortcut to initialize YOLO-World model with text prompts.   | [SAM2]                                                |
| `ultra.sam2-points`      | Shortcut to initialize YOLO-World model with text prompts.   | [SAM2]                                                |

### Snippet Example

<details><summary><code>ultra.yolo-model</code> Snippet</summary>
<p>

Drop-down select available for `version`, `scale`, and `task`, equivalent Python code shown below

```py
version = 8
scale = "s"
task = "."  # detect
model = YOLO(f"yolov{version}{scale}{task}pt")

version = 9
scale = "e"
task = "-seg."  # segment
model = YOLO(f"yolov{version}{scale}{task}pt")
```

**NOTE:** It will be possible to create combinations that aren't available, such as `yolov8n-worldv2.pt`. User is responsible for creating a valid configuration per documentation. 

</p></details>

## Utilities

| Alias                       | Description                                                                    | Reference                              |
| --------------------------- | ------------------------------------------------------------------------------ | -------------------------------------- |
| `ultra.util-auto-annotate`  | Use Ultralytics auto_annotate function to generate annotations.                | [`auto_annotator` fucntion][auto ann]  |
| `ultra.util-annotator`      | Use Ultralytics Annotator class to draw box annotations                        | [`Annotator` class][ann]               |
| `ultra.util-make-divisible` | Use Ultralytics make_divisible function to make a number divisible by another. | [`make_divisible` function][divisible] |
| `ultra.util-callback`       | Shortcut for adding custom model callback for a defined function.              | [`callbacks`][callbacks]               |

### Snippet Example

<details><summary><code>ultra.auto-annotate</code> Snippet</summary>
<p>

```py
from ultralytics.data.annotator import auto_annotate

auto_annotate(data="", det_model="yolov8n.pt", sam_model="sam_b.pt", device="cuda", output_dir="")
```

**NOTE**: Each function argument will be a "field" that can be tabbed into and changed. The `det_model`, `sam_model`, and `device` arguments will have options for default models, but can be cleared to input custom strings instead.

</p></details>

## Examples

The Example snippets are more "complete" blocks of code that can be used for boilerplate demonstrations.

| Prefix                               | Description                                                                                                     |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `ultra.example-predict-filter-class` | Ultralytics basic YOLO object detection predict with filtered classes example.                                  |
| `ultra.example-result-filter-class`  | Filter prediction results by class ID. Using "classes" keyword argument for prediction should be preferred.     |
| `ultra.example-yolo-predict`         | Setup Ultralytics YOLO to perform predict (simple).                                                             |
| `ultra.example-yolo-val`             | Setup Ultralytics YOLO to perform validation (simple).                                                          |
| `ultra.example-yolo-train`           | Setup Ultralytics YOLO to perform training (simple).                                                            |
| `ultra.example-yolo-predict-kwords`  | Setup Ultralytics YOLO to perform inference, show **all** inference keyword arguments and their default values. |
| `ultra.example-yolo-train-kwords`    | Setup Ultralytics YOLO for training, with **all** keyword arguments and their default values.                   |
| `ultra.example-sam-predict`          | Setup Ultralytics SAM to perform inference (simple).                                                            |
| `ultra.example-sam2`                 | Example showing use of SAM2 with bounding box and point prompts.                                                |
| `ultra.example-mobile-sam-predict`   | Setup Ultralytics MobileSAM to perform inference (simple).                                                      |
| `ultra.example-fast-sam-predict`     | Setup Ultralytics FastSAM to perform inference (simple).                                                        |
| `ultra.example-nas-predict`          | Setup Ultralytics NAS to perform inference (simple).                                                            |
| `ultra.example-rtdetr-predict`       | Setup Ultralytics RT-DETR to perform inference (simple).                                                        |
| `ultra.example-callback`             | Example showing how to add a custom callback function.                                                          |
| `ultra.example-track-loop-persist`   | Example of how to open video, loop frames, and maintain tracked object IDs.                                     |
| `ultra.example-track-kwords`         | Example showing all keyword arguments available for track mode.                                                 |

### Snippet Example

<details><summary><code>ultra.example-predict</code> Snippet</summary>
<p>

```py
from ultralytics import YOLO, ASSETS

model = YOLO("yolov8n.pt", task="detect")
results = model(source=ASSETS / "bus.jpg")

for result in results:
    print(result.boxes.data)
    # result.show()  # uncomment to view each result image
```

**NOTE**: Here, the only configurable option is the model scale which can be any one of: `n`, `s`, `m`, `l`, or `x`.

</p></details>

## KWARGS

Use these to insert the various model methods defined in [modes] with all keyword arguments, default values, and commented descriptions quickly into your code. Includes `model` as default variable, but is an editable field accessible using tab stops.

| Prefix                 | Description                                                                              | Reference  |
| ---------------------- | ---------------------------------------------------------------------------------------- | ---------- |
| `ultra.kwargs-predict` | Snippet using model `predict` method, including all keyword arguments and defaults.      | [predict]  |
| `ultra.kwargs-train`   | Snippet using model `train` method, including all keyword arguments and defaults.        | [train]    |
| `ultra.kwargs-track`   | Snippet using model `track` method, including all keyword arguments and defaults.        | [track]    |
| `ultra.kwargs-val`     | Snippet using model `val` method, including all keyword arguments and defaults.          | [val]      |

### Snippet Example

<details><summary><code>ultra.kwargs-predict</code></summary>
<p>

```py
model.predict(
    source=src,           # (str, optional) source directory for images or videos
    imgsz=640,            # (int | list) input images size as int or list[w,h] for predict
    conf=0.25,            # (float) minimum confidence threshold
    iou=0.7,              # (float) intersection over union (IoU) threshold for NMS
    vid_stride=1,         # (int) video frame-rate stride
    stream_buffer=False,  # (bool) buffer all streaming frames (True) or return the most recent frame (False)
    visualize=False,     # (bool) visualize model features
    augment=False,       # (bool) apply image augmentation to prediction sources
    agnostic_nms=False,  # (bool) class-agnostic NMS
    classes=None,        # (int | list[int], optional) filter results by class, i.e. classes=0, or classes=[0,2,3]
    retina_masks=False,  # (bool) use high-resolution segmentation masks
    embed=None,          # (list[int], optional) return feature vectors/embeddings from given layers
    show=False,          # (bool) show predicted images and videos if environment allows
    save=True,           # (bool) save prediction results
    save_frames=False,   # (bool) save predicted individual video frames
    save_txt=False,      # (bool) save results as .txt file
    save_conf=False,     # (bool) save results with confidence scores
    save_crop=False,     # (bool) save cropped images with results
    stream=False,        # (bool) for processing long videos or numerous images with reduced memory usage by returning a generator
    verbose=True,        # (bool) enable/disable verbose inference logging in the terminal
)
```

</p></details>

## Use with `neovim`

It's possible to use VS Code snippets by installing the [LuaSnip](https://github.com/L3MON4D3/LuaSnip) repo and then adding the following line into your configuration of `LuaSnip`:

```
require("luasnip.loaders.from_vscode").lazy_load({ paths = { "./ultralytics-snippets/" }, include = { "python" } })
```

Make sure that the path `"./ultralytics-snippets/"` is valid for your install location. 

> [!NOTE] 
> If the snippets don't work, try removing the comment lines at the top of each JSON file. These are ignored by VS Code, but might not be ignored by `neovim` or `LuaSnip`.


[ann]: https://docs.ultralytics.com/usage/simple-utilities/#drawing-annotations
[models]: https://docs.ultralytics.com/models
[modes]: https://docs.ultralytics.com/modes
[predict]: https://docs.ultralytics.com/modes/predict
[train]: https://docs.ultralytics.com/modes/train
[track]: https://docs.ultralytics.com/modes/track
[val]: https://docs.ultralytics.com/modes/val
[YOLOv8]: https://docs.ultralytics.com/models/yolov8
[YOLOv5]: https://docs.ultralytics.com/models/yolov5
[YOLOv9]: https://docs.ultralytics.com/models/yolov9
[YOLOv10]: https://docs.ultralytics.com/models/yolov10
[YOLO-World]: https://docs.ultralytics.com/models/yolo-world
[SAM]: https://docs.ultralytics.com/models/sam
[Mobile SAM]: https://docs.ultralytics.com/models/mobile-sam
[FastSAM]: https://docs.ultralytics.com/models/fast-sam
[YOLO-NAS]: https://docs.ultralytics.com/models/yolo-nas
[RTDETR]: https://docs.ultralytics.com/models/rtdetr
[SAM2]: https://docs.ultralytics.com/models/sam-2
[pred results]: https://docs.ultralytics.com/modes/predict/#working-with-results
[results class]: https://docs.ultralytics.com/reference/engine/results/
[auto ann]: https://docs.ultralytics.com/reference/data/annotator/
[divisible]: https://docs.ultralytics.com/reference/utils/ops/#ultralytics.utils.ops.make_divisible
[Model Export]: https://docs.ultralytics.com/modes/export
[callbacks]: https://docs.ultralytics.com/usage/callbacks/
