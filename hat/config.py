import torch 
from deepvac import config, AttrDict

config.disable_git = True
config.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

config.model_path = "/ your face det model path /"
config.confidence_threshold = 0.02
config.nms_threshold = 0.4
config.top_k = 5000
config.keep_top_k = 1
config.max_edge = 2000
config.rgb_means = (104, 117, 123)

config.input_image_dir = '/ your input image path /'

config.input_hat_mask_dir = '/ your hat mask path /'
config.input_hat_image_dir = '/ your hat(chartlet) image path /'

config.output_image_dir = '/ your output image path /'
config.output_anno_dir = '/ your output annotation path /'

config.perspect_image_dir = '/ your perspect image dir /'
config.perspect_mask_dir = '/ your perspect mask dir /'
config.perspect_num = 5

config.flip_image_dir = '/ your flip image dir /'
config.flip_mask_dir = '/ your flip mask dir /'

config.fusion_hat_mask_dir = '/ your fusion hat mask dir /'
config.fusion_clothes_mask_dir = '/ your fusion clothes mask dir /'
config.fusion_new_mask_dir = '/ your fusion new(fusion) mask dir /'

config.generate_input_hat_image_dir_from_cocoannotator = '/ your input hat image dir /'
config.generate_input_hat_mask_dir_from_cocoannotator = '/ your input hat mask dir /'
config.generate_output_hat_image_dir = '/ your output hat image dir /'
config.generate_output_hat_mask_dir = '/ your output hat mask dir /'
