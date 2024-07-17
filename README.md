# Ultralytics Snippets for VSCode

<div align="center">
  <p>
    <a href="https://github.com/ultralytics/assets/releases/tag/v8.2.0" target="_blank">
      <img width="80%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="YOLO Vision banner"></a>
  </p>
</div>

A [Python snippets extension for VSCode](https://marketplace.visualstudio.com/items?itemName=Ultralytics.ultralytics-snippets) to assist with development using the [Ultralytics package](https://github.com/ultralytics/ultralytics). These snippets will help you code with Ultralytics faster and help provide some boilerplate examples to test out. Open an Issue or a Pull Request to have your snippet added! 🚀

<div align="center">
  <p>
    <img src="https://github.com/Burhan-Q/ultralytics-snippets/assets/62214284/42ad0b17-e752-479c-9c6c-e451fffbe8b3" alt="Snippet Prediction Preview">
    <strong>NOTE:</strong> Tab-completion used to complete snippet and quickly hop into fields.
  </p>
</div>

## Installation

### From the Web

#### Method-1

1. Visit the VSCode Extension Market place by going to https://marketplace.visualstudio.com/VSCode and search for `Ultralytics-Snippets`.

#### Method-2

1. Follow [this link](https://marketplace.visualstudio.com/items?itemName=Ultralytics.ultralytics-snippets) to visit the extension page directly.

2. Click the "Install" button and allow your browser to launch a VSCode session.

    ![VSCode marketplace extension install](https://github.com/user-attachments/assets/b40cc8e2-2353-4165-859a-c84eec070db6)

### From VSCode

1. Navigate to the Extensions menu, and search for `Ultralytics-Snippets`.

2. Click the "Install" button.

    ![VSCode extension menu](https://github.com/user-attachments/assets/9de46d22-ef7b-4765-ba2c-d0459cafa4dc)

### From the CLI

You can also install the latest version of the `Ultralytics-Snippets` VSCode extension using the following command.

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
| `ultra.example-mobile-sam-predict`   | Setup Ultralytics MobileSAM to perform inference (simple).                                                      |
| `ultra.example-fast-sam-predict`     | Setup Ultralytics FastSAM to perform inference (simple).                                                        |
| `ultra.example-nas-predict`          | Setup Ultralytics NAS to perform inference (simple).                                                            |
| `ultra.example-rtdetr-predict`       | Setup Ultralytics RT-DETR to perform inference (simple).                                                        |

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



[ann]: https://docs.ultralytics.com/usage/simple-utilities/#drawing-annotations
[models]: https://docs.ultralytics.com/models
[_modes]: https://docs.ultralytics.com/modes
[_predict]: https://docs.ultralytics.com/modes/predict
[_train]: https://docs.ultralytics.com/modes/train
[_val]: https://docs.ultralytics.com/modes/val
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
[pred results]: https://docs.ultralytics.com/modes/predict/#working-with-results
[results class]: https://docs.ultralytics.com/reference/engine/results/
[auto ann]: https://docs.ultralytics.com/reference/data/annotator/
[divisible]: https://docs.ultralytics.com/reference/utils/ops/#ultralytics.utils.ops.make_divisible
[Model Export]: https://docs.ultralytics.com/modes/export