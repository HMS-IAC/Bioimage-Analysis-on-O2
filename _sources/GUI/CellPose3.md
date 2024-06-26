# Cellpose3

<div>
    <p float="left">
        <a href="http://cellpose.org" target="_blank">
            <img src="../_static/assets/logos/cellpose3.png" width="10%" />
        </a>
    </p>
</div>

*Version: 3*

---
## Introduction
<a href="http://cellpose.org" target="_blank">Cellpose</a> is a powerful bioimage analysis software developed in Python 3 for segmenting a variety of cellular structures in diverse image types, including fluorescence microscopy images and other biological microscopy data. It offers an easy-to-use interface with one-click image restoration for enhanced cellular segmentation, making it suitable for researchers and scientists working on cellular and subcellular level imaging. Users can install it via pip or try it directly on cellpose.org, making it accessible and versatile for different bioimaging needs.

**Keywords:**
```{tags} segmentation, image-annotation, machine-learning, denoising
```

<button class="custom-button">
  <a href="https://cellpose.readthedocs.io/en/latest/" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://github.com/mouseland/cellpose" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/cellpose" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
/n/app/bias/cellpose/cellpose3.sh -i 
```
or
```bash
/n/app/bias/cellpose/cellpose3.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult a conda environment is created inside your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/cellpose/cellpose3.sh -u
```
or
```bash
/n/app/bias/cellpose/cellpose3.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/cellpose/cellpose3.sh -h
```
or
```bash
/n/app/bias/cellpose/cellpose3.sh --help
```

---
## Using Cellpose3 on O2

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>Cellpose installation does include PyTorch so for accelerated inference, you can use GPU both for the GUI and for headless mode.</p>
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
One can use Cellpose through the command line interface (CLI). Instructions regarding the usage can be found <a href="https://cellpose.readthedocs.io/en/latest/command.html" target="_blank">here</a>. You will need to activate the cellpose environment first to use cellpose through CLI. If you used the default installation path, you can load the environement using the following command:
```bash
module load miniconda3/23.1.0
source activate cellpose
```
Alternatively, if you installed cellpose in a different path, then run the following command:
```bash
module load miniconda3/23.1.0
source activate -p <cellpose_installation_directory>/cellpose/env
```

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (2021). Cellpose: a generalist algorithm for cellular segmentation. Nature methods, 18(1), 100-106. <a href="https://doi.org/10.1038/s41592-020-01018-x" target="_blank">doi:10.1038/s41592-020-01018-x</a></p>
  <p><i>Find more information <a href="https://github.com/mouseland/cellpose?tab=readme-ov-file#citation" target="_blank">here</a>.</i></p>
</div>