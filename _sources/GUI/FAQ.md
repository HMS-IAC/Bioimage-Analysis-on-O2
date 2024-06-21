# FAQ

<div class="toggle-faq">
  <details>
    <summary><strong>How does the installation work?</strong></summary>
    <p>The bash scripts handle the installation of various bioimage analysis tools differently. For Fiji, QuPath, and Ilastik, it downloads the compressed files, extracts them into the Documents folder, and creates an executable on your Desktop. For Cellpose, PlantSeg, and Napari, the process is a bit more nuanced. The script sets up separate conda environments for each, installs the required packages, and then creates a dedicated folder in the Documents directory. It writes a Bash script in this folder that, when executed, activates the corresponding environment and launches the software. Finally, it generates an executable file on the Desktop for easy access.</p>
  </details>
</div>

<div class="toggle-faq">
  <details>
    <summary><strong>How do I use data stored on our lab’s shared drive?</strong></summary>
    <p>To access any data that’s on O2 (individual scratch, shared scratch, shared group folder, etc.), you first need to click on the checkboxes when you request Desktop Mate to access the storage. You can then go to Open folder → Computer → / → n</p>
    <p>Once you go to n, you will see all the folders. Next, you can follow the path trail to your folder.</p>
  </details>
</div>

<div class="toggle-faq">
  <details>
    <summary><strong>Where are the installation files stored?</strong></summary>
    <p>The installation files are stored inside the Documents folder.</p>
  </details>
</div>

<div class="toggle-faq">
  <details>
    <summary><strong>Can I use QuPath headlessly?</strong></summary>
    <p>Yes! QuPath has instructions on how to use it headlessly on <a href="https://qupath.readthedocs.io/en/stable/docs/advanced/command_line.html#">this FAQ page</a>. Specific subcommands can be found in <a href="https://qupath.readthedocs.io/en/stable/docs/advanced/command_line.html#">this sub-section</a>. For O2 specific installation, the QuPath executable file can be found at <em>~/Documents/QuPath/bin</em></p>
  </details>
</div>

<div class="toggle-faq">
  <details>
    <summary><strong>Does QuPath use GPU?</strong></summary>
    <p>By default, QuPath <strong>does not</strong> use GPU and only StarDist can take advantage of GPU access right now. You can find more information regarding that <a href="https://qupath.readthedocs.io/en/stable/docs/deep/gpu.html">here</a>.</p>
  </details>
</div>

<div class="toggle-faq">
  <details>
    <summary><strong>Can I use CellPose headlessly?</strong></summary>
    <p>Yes! You can find necessary information regarding that <a href="https://cellpose.readthedocs.io/en/latest/command.html">here</a>. For the CellPose executable, you will need to activate the CellPose environment first. You can do that using the following commands:</p>
    <pre style="background-color: #e0e0e0; padding: 10px; border-radius: 5px;"><code>module purge
module load miniconda3/23.1.0
source activate cellpose</code></pre>
  </details>
</div>