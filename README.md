# Asset Validation Tool (Blender Python)

A Python-based toolset built in Blender to automate common asset checks and small rig utilities.  
This project uses a stylized squid model as a test asset to explore Technical Artist / Pipeline TD workflows.

The repository includes:
- the original concept sketch
- a clean 3D asset
- a deliberately broken version of the model
- Python scripts used to validate and fix common production issues

---

## ✨ Features

### Model Checker
Automated validation checks for common asset problems:

- Naming convention checks  
- Transform validation (unapplied scale / rotation)  
- Polycount reporting  
- Flipped normals detection  
- UV existence check (detects missing UV maps)

Each check is designed to **flag issues early** before assets move further down the pipeline.

📹 Demo videos:
- Model Checker – Naming  
- Model Checker – Transform  
- Model Checker – Polycount  
- Model Checker – Normals  
- Model Checker – UV Check  

---

### Rig & Utility Tools
Small quality-of-life tools focused on rig consistency and testing:

- Automatic bone naming  
- Procedural “wiggle” bones for tail testing

📹 Demo videos:
- Naming Bones  
- Wiggle Bones  

---

## 🦑 Asset Overview

The squid model was intentionally kept simple to reflect how stylized assets are often handled in production.  
After creating a clean version, the asset was deliberately “broken” (bad names, transforms, normals, missing UVs) to test the validation tools.

📹 Squid Overall Preview

---

## 🎯 Project Goal

This project was created to explore the **Technical Artist / Pipeline TD role**, focusing on:
- asset validation
- workflow automation
- bridging art and code
- identifying common production-breaking issues

The emphasis is on **detection and feedback**, rather than auto-fixing everything.

---

## 📝 Concept Sketch

![Concept Sketch](./path-to-your-sketch-image.png)
