CUDA_VISIBLE_DEVICES=0,1,3 python3 train.py \
  --name audioVisual \
  --hdf5_path /home/manhnguyen/new/co-separation/dataset/sample_hdf5 \
  --batchSize 16 \
  --nThreads 32 \
  --display_freq 10  \
  --save_latest_freq 500 \
  --niter 2 \
  --validation_freq 200  \
  --validation_batches 20 \
  --num_batch 500000 \
  --lr_steps 15000 30000 \
  --checkpoints_dir 16_500000_checkpoint_dataD3_no_image \
  --classifier_loss_weight 0.05 \
  --coseparation_loss 1 \
  --unet_num_layers 7 \
  --lr_visual 0.00001 \
  --lr_unet 0.0001 \
  --lr_classifier 0.0001 \
  --weighted_loss \
  --visual_pool conv1x1 \
  --optimizer adam \
  --log_freq True \
  --tensorboard True \
  --gpu_ids 1,2 \
  --continue_train \
  --validation_visualization True |& tee -a log_16_500000_checkpoint_dataD3_no_image2.txt 
 
  # --with_additional_scene_image \
  #weight for continue train
  
  # --weights_visual /home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/visual_best.pth \
  # --weights_unet /home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/unet_best.pth \
  # --weights_classifier /home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/classifier_best.pth  \