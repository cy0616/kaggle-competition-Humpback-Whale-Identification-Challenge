# [kaggle-competition-Humpback-Whale-Identification-Challenge](https://www.kaggle.com/c/whale-categorization-playground#description)

本次竞赛要解决的问题是，通过识别图片中的鲸鱼尾巴，实现对鲸鱼种类的分类，属于一个多分类问题<br>
提供的数据集包括9850张训练图片（4251个种类）和15610张测试图片。<br>
这是本人第一次参加的比赛，最终以0.45426的分数，排名**45th**/528，top**9%**<br><br>

![avatar](https://kaggle2.blob.core.windows.net/competitions/kaggle/3333/media/happy-whale.jpg)
<br><br>

## 环境说明：
> tensorflow-gpu:1.4.1<br>
keras-gpu:2.0.5

## 文件说明：

- **input**:    notebook文件需要的输入<br>
  - humpback-whale-identification-model-files:    Whale Recognition Model with score 0.78563.ipynb需要的文件<br>
  - train.csv:    原始训练集标注文件<br>
  - train_aug.csv:    Keras_lb_0.38_to_0.42_cut_aug.py使用的经过裁剪，以及数据增强后的训练集标准文件<br>
  - original_image.csv:    测试集中与训练重复的鲸鱼图片（生成测试数据时，这些结果相当于提前知道答案的）<br>
  - annotations_9850.csv:    使用RetinaNet进行Object Detection后，对训练集定位的结果（存在5%的错误）<br>
- **notebook**:    .ipynb和.py文件，不同的方法所对应的代码文件，具体代码所用的方法在下面给出说明：<br>
  - Whale Prediction Using Resnet-50.ipynb    :使用Resnet-50作为基础网络模型，输入数据为三元组，损失函数为三元组损失，使用imgnet预训练模型，生成test数据使用KNN。<br>
  - Keras_lb_0.38.py:    在上面的基础上做出少量改动。<br>
  - Keras_lb_0.38_to_0.42.py:    在上面的基础上，生成test使用欧氏距离（并没有什么提升），在生成测试数据时修改new_whale类别的权重为0.00（越小代表距离越近），并且保证如果有原图，则原图作为第一结果输出，其他情况，new_whale作为第一结果输出，score会达到0.42<br>
  - Keras_lb_0.38_to_0.42_cut_aug.py:    在上面的基础上，使用经过裁剪（使用RetinaNet进行Object Detection），以及数据增强后的训练集来训练模型（triplet_model_cut_aug_weights.best.hdf5）用裁剪后的测试集生成测试数据，调整new_whale类别的权重，并将生成的结果与测试集中存在训练集原图的情况进行合并（original_image.csv）<br>
  - Whale Recognition Model with score 0.78563.ipynb:    本次比赛第一名的做法，已经将个人的理解以及部分步骤的解释写入该文件中，使用孪生网络，并且在生成用于训练的训练图片对时，有很大的技巧，在判断测试集与训练集的重复图片时，使用哈希感知。
- **checkpoint**:    存放训练好的模型<br>
  - triplet_model_cut_aug_weights.best.hdf5:    经过裁剪，以及数据增强后的训练集来训练模型<br>
  - resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5:    ImageNet预训练模型<br>
- **utils**:    其他工具脚本
  - merge_original_img.py:    将eras_lb_0.38_to_0.42_cut_aug.py生成的测试结果与测试集中重复的鲸鱼图片融合。


