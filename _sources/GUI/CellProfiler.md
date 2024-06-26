# CellProfiler

<div>
    <p float="left">
        <a href="https://cellprofiler.org/" target="_blank">
            <img src="../_static/assets/logos/cellprofiler.png" width="10%" />
        </a>
    </p>
</div>

*Version: 4.2.6*

---
## Introduction
<a href="https://cellprofiler.org/" target="_blank">CellProfiler</a> is a free, open-source software designed for the quantitative analysis of biological images. It allows biologists, even those without expertise in computer vision or programming, to measure cell or whole-organism phenotypes from thousands of images automatically. Users create an analysis pipeline using modules to identify cells and their compartments, measuring various features to generate a comprehensive, quantitative dataset. While the software provides general and successful methods by default, users can customize these settings and leverage basic image analysis algorithms to tackle more complex challenges. Extensible through plugins in Python or for ImageJ, CellProfiler excels in analyzing cells, neurons, C. elegans, 2D fluorescent images, high-throughput screening, phenotype classification, and handling multiple stains per site. However, it is primarily limited to 2D images, is not ideal for manually-guided analysis, and has image size limitations.

**Keywords:**
```{tags} image-processing, high-content-screening, segmentation, machine-learning
```

<button class="custom-button">
  <a href="https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.6/index.html" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://github.com/CellProfiler/CellProfiler" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/cellprofiler" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
/n/app/bias/cellprofiler/cellprofiler.sh -i 
```
or
```bash
/n/app/bias/cellprofiler/cellprofiler.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult a conda environment is created inside your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/cellprofiler/cellprofiler.sh -u
```
or
```bash
/n/app/bias/cellprofiler/cellprofiler.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/cellprofiler/cellprofiler.sh -h
```
or
```bash
/n/app/bias/cellprofiler/cellprofiler.sh --help
```

---
## Using Cellpose3 on O2


### Using the GUI
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).


<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>


Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.


### Using in headless mode
One can use CellProfiler through the command line interface (CLI) for batch processing. Instructions regarding the usage can be found <a href="https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.6/help/other_batch.html?highlight=headless" target="_blank">here</a>. You will need to activate the cellprofiler environment first to use cellpose through CLI. If you used the default installation path, you can load the environement using the following command:
```bash
module load miniconda3/23.1.0
source activate $HOME/Documents/cellprofiler/env
```
Alternatively, if you installed cellpose in a different path, then run the following command:
```bash
module load miniconda3/23.1.0
source activate -p </path/to/your/cellprofiler/installation>/cellprofiler/env
```

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Stirling, D.R., Swain-Bowden, M.J., Lucas, A.M. et al. CellProfiler 4: improvements in speed, utility and usability. BMC Bioinformatics 22, 433 (2021).<a href="https://doi.org/10.1186/s12859-021-04344-9" target="_blank">doi:10.1186/s12859-021-04344-9</a></p>
  <p><i>Find more information <a href="https://cellprofiler.org/citations" target="_blank">here</a>.</i></p>
</div>