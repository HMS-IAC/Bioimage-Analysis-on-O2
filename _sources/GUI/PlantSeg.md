# PlantSeg

<div>
    <p float="left">
        <img src="../_static/assets/logos/plantseg.png" width="10%" />
    </p>
</div>

---
## Introduction
<a href="https://github.com/kreshuklab/plant-seg" target="_blank">Cellpose</a> is a bioimage analysis software designed for cell instance-aware segmentation in densely packed 3D volumetric images. It employs a two-stage segmentation strategy, combining neural network predictions with advanced segmentation techniques to achieve precise results. PlantSeg is particularly optimized for plant cell tissues, making it an ideal tool for analyzing images acquired through confocal and light sheet microscopy. With the provision of pre-trained models, users can efficiently segment complex plant tissues, facilitating detailed and accurate biological analysis.

**Keywords:**
```{tags} segmentation, machine-learning
```

<button class="custom-button">
  <a href="https://kreshuklab.github.io/plant-seg/" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://github.com/kreshuklab/plant-seg?tab=readme-ov-file" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>

---
## Options
```-h / --help```: Display help.

```-i / --install```: Install and create .desktop executible.

```-u / --uninstall```: Uninstall and remove all dependencies.

```-p / --path``` *(optional)*: Specify the installation directory. Default is $HOME/Documents

---
## Installation instruction
### Login to a compute node
1. Use the instructions below to log in to a login node:
    1. **Using terminal on local computer:** You can find a comprehensive instructions provided by RC [here](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/1601700123/How+to+login+to+O2) on how to use a terminal to SSH into a login node. Depending on the operating system on your laptop, you may need to perform different steps.
    2. **Using a browser** *(Chrome recommended)*: Alternatively, you can also go to [this link](https://o2portal.rc.hms.harvard.edu/pun/sys/shell/ssh/o2.hms.harvard.edu) to login to an O2 shell via browser. Detailed instructions are provided [here](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2234581082/Open+an+O2+command+line+terminal).
2. Once you log in, run the following command to request compute access:

```bash
srun --pty -p interactive -t 0-4:00 --mem 16g bash
```

### Run Installer
#### To **install**:
```bash
/n/app/bias/plantseg/plantseg.sh -i
```
or
```bash
/n/app/bias/plantseg/plantseg.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult a conda environment is created inside your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/plantseg/plantseg.sh -u
```
or
```bash
/n/app/bias/plantseg/plantseg.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/plantseg/plantseg.sh -h
```
or
```bash
/n/app/bias/plantseg/plantseg.sh --help
```

---
## Using PlantSeg on O2

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>PlantSeg installation does include PyTorch so for accelerated inference, you can use GPU both for the GUI and for headless mode.</p>
</div>

### Using the GUI
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).


<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>


Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.


### Using in headless mode
One can use PlantSeg through the command line interface (CLI). Instructions regarding the usage can be found <a href="https://kreshuklab.github.io/plant-seg/chapters/plantseg_classic_cli/" target="_blank">here</a>. You will need to activate the plantseg environment first to use cellpose through CLI. If you used the default installation path, you can load the environement using the following command:
```bash
module load miniconda3/23.1.0
source activate plantseg
```
Alternatively, if you installed cellpose in a different path, then run the following command:
```bash
module load miniconda3/23.1.0
source activate -p <plantseg_installation_directory>/plantseg/env
```

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Wolny, A., Cerrone, L., Vijayan, A., Tofanelli, R., Barro, A. V., Louveaux, M., Wenzl, C., Strauss, S., Wilson-Sánchez, D., Lymbouridou, R., Steigleder, S. S., Pape, C., Bailoni, A., Duran-Nebreda, S., Bassel, G. W., Lohmann, J. U., Tsiantis, M., Hamprecht, F. A., Schneitz, K., Maizel, A., … Kreshuk, A. (2020). Accurate and versatile 3D segmentation of plant tissues at cellular resolution. eLife, 9, e57613. <a href="https://doi.org/10.7554/eLife.57613" target="_blank">doi:10.7554/eLife.57613</a></p>
  <p><i>Find more information <a href="https://github.com/kreshuklab/plant-seg?tab=readme-ov-file#citation" target="_blank">here</a>.</i></p>
</div>