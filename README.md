# Asset Validation Tool (Blender Python)

A Python-based toolset built in Blender to automate common asset checks and small rig utilities.  
This project uses a stylized squid model as a test asset to explore Technical Artist / Pipeline TD workflows.

The repository includes:
- original concept sketches
- a clean 3D asset
- a deliberately broken version of the model
- Python scripts used to validate and test assets

---

## ✨ Features

### Model Checker
Automated validation checks for common asset problems:

- Naming convention checks  
- Transform validation (unapplied scale / rotation)  
- Polycount reporting  
- Flipped normals detection  
- UV existence check (detects missing UV maps)

**Demos**

**Naming Convention Check**  
![Naming Check](Model_Checker/Gif/Model%20Checker%20(Naming).gif)

**Transform Validation**  
![Transform Check](Model_Checker/Gif/Model%20Checker%20(Transform).gif)

**Polycount Check**  
![Polycount Check](Model_Checker/Gif/Model%20Checker%20(Polygon).gif)

**Normals Check**  
![Normals Check](Model_Checker/Gif/Model%20Checker%20(Normals).gif)

**UV Existence Check**  
![UV Check](Model_Checker/Gif/Model%20Checker%20(UV).gif)

---

### Rig & Utility Tools

Small quality-of-life tools focused on rig consistency and testing:

**Automatic Bone Naming**  
![Naming Bones](Model_Checker/Gif/Naming%20Bones.gif)

**Procedural Wiggle Bones (Tail Test)**  
![Wiggle Bones](Model_Checker/Gif/Wiggle%20Bones.gif)

---

## 🦑 Asset Overview

The squid model was intentionally kept simple to reflect stylized production assets.  
After creating a clean version, the asset was deliberately “broken” to test the validation tools.

![Squid Overall](Model_Checker/Gif/Squid%20Overall.gif)

---

## 🎯 Project Goal

This project was created to explore the **Technical Artist / Pipeline TD role**, with a focus on:
- asset validation
- workflow automation
- bridging art and code
- detecting common production-breaking issues early

The emphasis is on **detection and feedback**, rather than automatic fixing.

---

## 📝 Concept Sketch

**Initial Sketch**  
![Concept Sketch](Model_Checker/Image/Sketch.jpeg)

**Additional Drawing**  
![Drawing](Model_Checker/Image/Drawing.jpeg)
