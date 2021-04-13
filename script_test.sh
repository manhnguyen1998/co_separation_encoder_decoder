CUDA_VISIBLE_DEVICES=2 python test.py \
--video1_name 9dOqmTMqp1k_4 \
--video2_name X3GbAKww1KI_4 \
--visual_pool conv1x1 \
--hdf5_path /home/manhnguyen/new/co-separation/iccv2019_co_separation/iccv2019_co_separation/sample_hdf5/test.h5 \
--unet_num_layers 7 \
--data_path /home/manhnguyen/new/co-separation \
--weights_visual /home/manhnguyen/new/co-separation/checkpoints/audioVisual/visual_latest.pth \
--weights_unet /home/manhnguyen/new/co-separation/checkpoints/audioVisual/unet_latest.pth \
--weights_classifier /home/manhnguyen/new/co-separation/checkpoints/audioVisual/classifier_latest.pth  \
--num_of_object_detections_to_use 5 \
--scene_path /home/manhnguyen/new/co-separation/iccv2019_co_separation/iccv2019_co_separation/ADE.h5 \
--output_dir_root results2/ \
# --with_additional_scene_image \
# -- gpu