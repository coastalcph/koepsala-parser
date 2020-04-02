import os,sys
#run:
# python send_all_jobs.py data_dir checkpoints
# where data dir contains the UD directory and checkpoints
# will save checkpoints with one directory per treebank, 
# named after its iso


#ISO_TODO = ['sv_talbanken', 'en_ewt', 'lv_lvtb', 'cs_fictree',
#'cs_pdt', 'it_isdt', 'uk_iu', 'pl_pdb','ru_syntagrus',
#'sk_snk','nl_alpino', 'nl_lassysmall', 'et_ewt']
#ISO_TODO = ['cs_cac', 'ar_padt', 'fi_tdt']
#ISO_TODO += ['cs_cac', 'ar_pdt', 'fi_tdt']
ISO_TODO=['cs_cac', 'ar_padt', 'fi_tdt']

eud_dir=sys.argv[1]
chkpoints = sys.argv[2]
langs = os.listdir(eud_dir)
for lang in langs:
    if lang.endswith('PUD') or lang.endswith('FQB'):
        continue
    iso_cmd = f'ls {eud_dir}{lang}/*train.conllu'
    iso = [line for line in os.popen(iso_cmd)][0].split("/")[7].split("-")[0]
    #not running jobs for the ones we already have a model for
    #if os.path.exists(f'{chkpoints}/{iso}/best.th'):
    #    continue
    # if not ISO_TODO or iso in ISO_TODO:
    #     if iso == 'et_ewt':
    #         send_cmd = f'sbatch --job-name {iso} bash/train_ud.sh {lang} {iso} {chkpoints}/{iso} /image/nlp-datasets/iwpt20/et_split/'
    #     else:
    if not ISO_TODO or iso in ISO_TODO:
        send_cmd = f'sbatch --job-name {iso} bash/train_ud.sh {lang} {iso} {chkpoints}/{iso}'
        os.system(send_cmd)
