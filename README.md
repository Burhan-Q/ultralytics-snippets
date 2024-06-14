# Ultralytics Snippets for VSCode

A python snippets extension for VSCode to assist with development using the Ultralytics package. 

## Syntax

All snippets use the format:

<p style="text-indent:13px;">
<code>{PREFIX}.{ROOT}*-{DESCRIPTOR}</code>
</p>

- `{PREFIX}` is always `ultra`

- `{ROOT}` denotes a common "root" verb or noun such as `import` or `results`. There will always be _at least one_ root common with other snippets, but it's possible there could be more than one, such as `results-boxes`.

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

## Results

These snippets will provide shortcuts for working with `ultralytics.engine.results.Results` objects returned from model inference. See the [Working with Results][pred results] of the documentation and the [Results class] reference page for more information.

| Alias                          | Description                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `ultra.results-class-strings`  | Convert class indices to class string names for a single image result.                                           |
| `ultra.results-data`           | Get result data array of detections from a single image result.                                                  |
| `ultra.results-loop`           | Iterate prediction results from an Ultralytics model.                                                            |
| `ultra.results-boxes-xyxy`     | Get pixel-value (x1, y1, x2, y2) bounding box coordinates from a single image result.                            |
| `ultra.results-boxes-xywh`     | Get pixel-value (x-center, y-center, w, h) bounding box coordinates from a single image result.                  |
| `ultra.results-masks-binary`   | Get binary segmentation masks from a single image result. NOTE: [N, H, W] shape, with inference H, W dimensions. |
| `ultra.results-masks-contours` | Get segmentation contours with pixel value xy or normalized xyn coordinates.                                     |
| `ultra.results-obb-xywhr`      | Get OBB rotated bounding boxes in pixel value [x, y, w, h, r] coordinates as torch.Tensor array.                 |
| `ultra.results-orig-image`     | Get original image from a single image result.                                                                   |

### Snippet Example

<details><summary><code>ultra.results-loop</code> Snippet</summary>
<p>

```py
for result in results:
    result.boxes.data  # torch.Tensor array
```

</p></details>

## Models

Quickly set up an [Ultralytics model][models], like [YOLOv8] to work with for various [modes][_modes]. 

| Alias                      | Description                                        | Reference                |
| -------------------------- | -------------------------------------------------- | ------------------------ |
| `ultra.yolo-predict`       | Setup Ultralytics YOLO to perform inference.       | [predict mode][_predict] |
| `ultra.yolo-val`           | Setup Ultralytics YOLO to perform validation.      | [val mode][_val]         |
| `ultra.yolo-train`         | Setup Ultralytics YOLO to perform training.        | [train mode][_train]     |
| `ultra.sam-predict`        | Setup Ultralytics SAM to perform inference.        | [SAM]                    |
| `ultra.mobile-sam-predict` | Setup Ultralytics MobileSAM to perform inference.  | [Mobile SAM]             |
| `ultra.fast-sam-predict`   | Setup Ultralytics FastSAM to perform inference.    | [FastSAM][fast sam]      |
| `ultra.nas-predict`        | Setup Ultralytics NAS to perform inference.        | [YOLO NAS]               |
| `ultra.rtdetr-predict`     | Setup Ultralytics RT-DETR to perform inference.    | [RTDETR]                 |

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

| Alias                  | Description                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| ultra.example-predict  | Ultralytics basic YOLO object detection predict example.                                                         |

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

**NOTE**: Here, the only configurable option is the model scale, `n`, `s`, `m`, `l`, or `x`.

</p></details>



[ann]: https://docs.ultralytics.com/usage/simple-utilities/#drawing-annotations
[models]: https://docs.ultralytics.com/models
[_modes]: https://docs.ultralytics.com/modes
[_predict]: https://docs.ultralytics.com/modes/predict
[_train]: https://docs.ultralytics.com/modes/train
[_val]: https://docs.ultralytics.com/modes/val
[yolov8]: https://docs.ultralytics.com/models/yolov8
[sam]: https://docs.ultralytics.com/models/sam
[mobile sam]: https://docs.ultralytics.com/models/mobile-sam
[fast sam]: https://docs.ultralytics.com/models/fast-sam
[yolo nas]: https://docs.ultralytics.com/models/yolo-nas
[rtdetr]: https://docs.ultralytics.com/models/rtdetr
[pred results]: https://docs.ultralytics.com/modes/predict/#working-with-results
[results class]: https://docs.ultralytics.com/reference/engine/results/
[auto ann]: https://docs.ultralytics.com/reference/data/annotator/
[divisible]: https://docs.ultralytics.com/reference/utils/ops/#ultralytics.utils.ops.make_divisible
