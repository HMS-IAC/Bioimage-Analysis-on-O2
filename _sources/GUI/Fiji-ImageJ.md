# Fiji-ImageJ

<div>
    <p float="left">
        <a href="https://fiji.sc" target="_blank">
            <img src="../_static/assets/logos/fiji.png" width="10%" />
        </a>
    </p>
</div>

---
## Introduction
<a href="https://fiji.sc" target="_blank">FIJI (Fiji Is Just ImageJ)</a> is an open-source bioimage analysis software widely used in the scientific community for processing and analyzing biological images. Built on the robust ImageJ platform, FIJI enhances ImageJ's capabilities with a comprehensive suite of plugins, tools, and scripting options tailored for advanced image analysis. Researchers and biologists leverage FIJI for tasks such as image segmentation, feature extraction, and 3D reconstruction, making it an indispensable tool in fields like microscopy, cell biology, and medical imaging. Its user-friendly interface, extensive documentation, and active community support further solidify FIJI's role as a go-to resource for bioimage analysis.

**Functions:**
```{tags} data-viewer, image-processing, segmentation, feature-extraction, object-tracking, image-annotation
```

<!-- .. tags::
   :tags: 2D viewer
   :tags: 3D viewer
   :tags: image processing -->

<button class="custom-button">
  <a href="https://imagej.net/ij/docs/index.html" target="_blank"><i class="fas fa-book"></i>   Documentation </a>
</button>
<button class="custom-button">
  <a href="https://imagej.net/plugins/" target="_blank"><i class="fas fa-puzzle-piece"></i>   Plugins </a>
</button>
<button class="custom-button">
  <a href="https://forum.image.sc/tag/fiji" target="_blank"><img src="../_static/assets/logos/forum_w.png" width="20px"/>   Forum </a>
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
/n/app/bias/fiji-imagej/fiji-imagej.sh -i
``` 
or
```bash
/n/app/bias/fiji-imagej/fiji-imagej.sh --install
```
<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>By deafult all Fiji files are copied to your home directory on O2. However, as the space of the home directory is limited, we recommend you specify a path (scratch or lab folder) by adding <code>-p</code> or <code>--path</code> as your input argument where all the files will be stored.</p>
</div>

#### To **uninstall**:
```bash
/n/app/bias/fiji-imagej/fiji-imagej.sh -u
```
or
```bash
/n/app/bias/fiji-imagej/fiji-imagej.sh --uninstall
```

#### For **help**:
```bash
/n/app/bias/fiji-imagej/fiji-imagej.sh -h
```
or
```bash
/n/app/bias/fiji-imagej/fiji-imagej.sh --help
```

---
## Using Fiji on O2
Once the installation is complete, you can verify that everything is set up correctly by logging into [Desktop Mate](https://o2portal.rc.hms.harvard.edu/pun/sys/dashboard/batch_connect/sys/RC_desktop_mate/session_contexts/new). If you're unsure how to do this, please refer to this [HMS RC guide on logging into Desktop Mate](https://harvardmed.atlassian.net/wiki/spaces/O2/pages/2235006977/How+to+use+HMS+RC+Desktop+App).

<div class="admonition tip">
  <p class="admonition-title">Tip</p>
  <p>We recommend using <strong>at least 16GB of memory</strong>. If you're working with larger images or tasks that require more resources, please allocate additional memory as necessary.</p>
</div>

Upon logging in, you'll find an icon on your desktop displaying the software’s logo and name. To launch the software, simply double-click this icon. The software is permanently installed on our Desktop Mate environment, meaning you only need to install it once. It will remain available for future sessions, just like software installed on your local computer.

When you're finished using the software, you can log out. The next time you need it, just log back in, and it will be ready to use again.

---
<div class="admonition note">
  <p class="admonition-title">Reference</p>
  <p>Schindelin, J., Arganda-Carreras, I., Frise, E., Kaynig, V., Longair, M., Pietzsch, T., … Cardona, A. (2012). Fiji: an open-source platform for biological-image analysis. Nature Methods, 9(7), 676–682. <a href="https://doi.org/10.1038/nmeth.2019" target="_blank">doi:10.1038/nmeth.2019</a></p>
  <p><i>Find more information <a href="https://imagej.net/contribute/citing" target="_blank">here</a>.</i></p>
</div>