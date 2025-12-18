Write-Host "Setting up the environment..."

# Check for Python
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed. Please install Python first."
    exit 1
}

# Install Python requirements
Write-Host "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

# Install Icarus Verilog using Winget
Write-Host "Checking for Icarus Verilog..."
if (-not (Get-Command "iverilog" -ErrorAction SilentlyContinue)) {
    Write-Host "Icarus Verilog not found. Attempting to install via Winget..."
    # Search and install Icarus Verilog. ID might vary, but 'bleyer.IcarusVerilog' or just 'Icarus Verilog' are common.
    # Using 'IcarusVerilog.IcarusVerilog' or searching for it.
    # To be safe, we try a likely ID.
    winget install --id "bleyer.iverilog" -e --source winget --accept-source-agreements --accept-package-agreements
    
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "Winget installation might have failed or the package ID changed. Please install Icarus Verilog manually from http://iverilog.icarus.com/"
    } else {
        Write-Host "Icarus Verilog installed successfully. You may need to restart your terminal."
    }
} else {
    Write-Host "Icarus Verilog is already installed."
}

Write-Host "Setup complete!"
