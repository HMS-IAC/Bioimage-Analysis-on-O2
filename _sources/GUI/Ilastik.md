# Ilastik

<div>
    <p float="left">
        <a href="https://www.ilastik.org" target="_blank">
            <img src="../_static/assets/logos/ilastik.png" width="10%" />
        </a>
    </p>
</div>

*Version: 1.4.0.post1*

---
## Introduction
<a href="https://www.ilastik.org" target="_blank">Ilastik</a> is a versatile, user-friendly bioimage analysis software designed to facilitate the segmentation, classification, and tracking of various biological images. Its intuitive graphical interface allows researchers to perform sophisticated image processing tasks without the need for extensive programming knowledge. ilastik is particularly well-suited for analyzing fluorescence microscopy images, histology slides, and other complex biological datasets, making it an invaluable tool for researchers in fields such as cell biology, neuroscience, and developmental biology.

**Keywords:**
```{tags} segmentation, object-classification, pixel-classification, counting, feature-extraction, object-tracking, image-annotation, digital-histology, machine-learning
```

<button class="custom-button">
  <a href="https://www.ilastik.org/documentation/" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://github.com/ilastik/ilastik" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/ilastik" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
/n/app/bias/ilastik/ilastik-1.4.0.sh -i
```
or
```bash
/n/app/bias/ilastik/ilastik-1.4.0.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult a conda environment is created inside your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>


#### To **uninstall**:
```bash
/n/app/bias/ilastik/ilastik-1.4.0.sh -u
```
or
```bash
/n/app/bias/ilastik/ilastik-1.4.0.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/ilastik/ilastik-1.4.0.sh -h
```
or
```bash
/n/app/bias/ilastik/ilastik-1.4.0.sh --help
```

---
## Using ilastik on O2

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>Ilastik installation does include PyTorch so for accelerated inference, you can use GPU both for the GUI and for headless mode.</p>
</div>


### Using GUI
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>

Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.

### Using headlessly
You can use ilastik in headless mode for batch processing. More information can be found <a href="" target="_blank">here</a>. For O2 specific installation, you will need to first activate the conda environemnt. To do so, you will need to run the following commands:
```bash
module purge
module load miniconda3/23.1.0
source activate -p <ilastik_installation_directory>/ilastik/env
```
The default installataion directory is ```$HOME/Documents```.

### Using Python
Ilastic API can now be accessed through Python as well. Example notebook can be found on their <a href="https://github.com/ilastik/ilastik/tree/main/notebooks" target="_blank">GitHub repo</a>. On O2, you can use the <a href="https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_jupyter/session_contexts/new" target="_blank">Jupyter app</a> to do the same. Specify the **Modules to be preloaded** as ```miniconda3/23.1.0``` and **Jupyter Environment** as ```source activate -p <ilastik_installation_directory>/ilastik/env```.

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Berg, S., Kutra, D., Kroeger, T. et al. ilastik: interactive machine learning for (bio)image analysis. Nat Methods 16, 1226–1232 (2019).<a href="https://doi.org/10.1038/s41592-019-0582-9" target="_blank">doi:10.1038/s41592-019-0582-9</a></p>
  <p><i>Find more information <a href="https://www.ilastik.org/publications" target="_blank">here</a>.</i></p>
</div>