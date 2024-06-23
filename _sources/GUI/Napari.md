# Napari

<div>
    <p float="left">
        <a href="https://napari.org/stable/" target="_blank">
            <img src="../_static/assets/logos/napari.png" width="10%" />
        </a>
    </p>
</div>

## Introduction
<a href="https://napari.org/stable/" target="_blank">Napari</a> is a powerful, interactive, and user-friendly bioimage analysis software designed specifically for Python. It excels in browsing, annotating, and analyzing large multi-dimensional images, making it ideal for complex datasets in biological research. Napari is built on top of Qt for its graphical user interface (GUI), vispy for efficient GPU-based rendering, and leverages the scientific Python stack, including numpy and scipy. With its robust support for multi-dimensional data, layering, and annotation, napari is particularly well-suited for handling images such as 3D fluorescence microscopy, time-lapse imaging, and other high-dimensional biological datasets. Its seamless integration with leading machine learning and image analysis tools, like scikit-image, scikit-learn, TensorFlow, and PyTorch, enhances its capability for advanced, automated analysis.

**Supported image dimensiions:**
```{tags} nD, data-viewer, segmentation, image-annotation
```

<button class="custom-button">
  <a href="https://github.com/napari/napari?tab=readme-ov-file" target="_blank"><i class="fa-brands fa-github"></i>   GitHub </a>
</button>
<button class="custom-button">
  <a href="https://www.napari-hub.org" target="_blank"><i class="fas fa-puzzle-piece"></i>   Plugins (napari hub) </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/napari" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
/n/app/bias/napari/napari.sh -i
```
or
```bash
/n/app/bias/napari/napari.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult a conda environment is created inside your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/napari/napari.sh -u
```
or
```bash
/n/app/bias/napari/napari.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/napari/napari.sh -h
```
or
```bash
/n/app/bias/napari/napari.sh --help
```

---
## Using napari on O2
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>

Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.

<div class="admonition attention">
  <p class="admonition-title">Attention</p>
  <p>napari uses PyQt for the GUI which may sometimes fail to work on Desktop Mate. Additionally, some of the napari plugins use OpenGL that could throw error while execution. If you run into any issue, please reach out.</p>
</div>

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>napari contributors (2019). napari: a multi-dimensional image viewer for python. <a href="https://zenodo.org/record/3555620" target="_blank">doi:10.5281/zenodo.3555620</a></p>
  <p><i>Find more information <a href="https://github.com/napari/napari?tab=readme-ov-file#citing-napari" target="_blank">here</a>.</i></p>
</div>