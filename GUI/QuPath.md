# QuPath

<div>
    <p float="left">
        <img src="../_static/assets/logos/qupath.png" width="10%" />
    </p>
</div>

---
## Introduction
<a href="https://qupath.github.io" target="_blank">QuPath</a> QuPath is an open-source bioimage analysis software designed for digital pathology and whole slide image analysis. It is particularly well-suited for working with large, high-resolution images typical in histology and pathology, including brightfield and fluorescence microscopy images. QuPath offers advanced tools for image segmentation, cell detection, and quantitative analysis, making it an invaluable resource for researchers in the biomedical field aiming to extract meaningful insights from complex biological images.

**Keywords:**
```{tags} segmentation, image-processing, pixel-classification, image-annotation, digital-histology, machine-learning
```

<button class="custom-button">
  <a href="https://qupath.readthedocs.io/en/0.5/" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://github.com/qupath/qupath" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/qupath" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
    1. **Using terminal on local computer:** You can find a comprehensive instructions provided by RC here on how to use a terminal to SSH into a login node. Depending on the operating system on your laptop, you may need to perform different steps.
    2. **Using a browser** *(Chrome recommended)*: Alternatively, you can also go to [this link](https://o2portal.rc.hms.harvard.edu/pun/sys/shell/ssh/o2.hms.harvard.edu) to login to an O2 shell via browser. Detailed instructions are provided [here](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2234581082/Open+an+O2+command+line+terminal).
2. Once you log in, run the following command to request compute access:

```bash
srun --pty -p interactive -t 0-4:00 --mem 16g bash
```

### Run Installer
#### To **install**:
```bash
/n/app/bias/qupath/qupath.sh -i
```
or
```bash
/n/app/bias/qupath/qupath.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult all QuPath files are copied to your home directory. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/qupath/qupath.sh -u
```
or
```bash
/n/app/bias/qupath/qupath.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/qupath/qupath.sh -h
```
or
```bash
/n/app/bias/qupath/qupath.sh --help
```

## Using QuPath on O2
### Using the GUI
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>

Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.

### Using headlessly
Scripts can be executed headlessly in QuPath via the command line. Information on how to use QuPath headlessly can be found on QuPath's <a href="https://qupath.readthedocs.io/en/latest/docs/advanced/command_line.html">documentation website</a>. On O2, you can locate the QuPath executible under <code>&lt;qupath_installation_directory&gt;/QuPath/bin</code>.

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Bankhead, P. et al. QuPath: Open source software for digital pathology image analysis. Scientific Reports (2017). <a href="https://doi.org/10.1038/s41598-017-17204-5" target="_blank">doi:10.1038/s41598-017-17204-5</a></p>
  <p><i>Find more information <a href="https://qupath.readthedocs.io/en/latest/docs/intro/citing.html" target="_blank">here</a>.</i></p>
</div>