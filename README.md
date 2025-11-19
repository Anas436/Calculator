# Calculator

A sleek, responsive, and user-friendly calculator application built with Python and Kivy, designed to showcase modern mobile app development skills.

## 📸 Application Preview

<center>![](https://github.com/Anas436/Calculator/blob/main/assets/Multiply.png)</center>

<center>![](https://github.com/Anas436/Calculator/blob/main/assets/Answer.png)</center>

## 🚀 Features

- **Clean & Intuitive UI**: Dark-themed interface with large, easy-to-read display
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Error Prevention**: Smart input validation prevents invalid expressions
- **Cross-Platform Compatibility**: Runs on Android, iOS, Windows, Linux, and macOS
- **Real-time Calculation**: Instant results with proper mathematical evaluation
- **Professional Design**: Polished button layout with optimal spacing and feedback

## 🛠️ Technical Stack

- **Framework**: Kivy 2.3.1
- **Language**: Python 3
- **Build Tool**: Buildozer
- **Architecture**: Object-oriented design with event-driven programming

## 📱 Key Implementation Details

### Smart Input Handling
```python
# Prevents multiple consecutive operators
if current and (self.last_was_operator and button_text in self.operators):
    return
# Prevents starting with operators
elif current == "" and button_text in self.operators:
    return
```

### Responsive Layout System
- Dynamic BoxLayout organization
- Consistent spacing and alignment
- Scalable font sizes for different screen resolutions

### Professional Code Structure
- Clean separation of concerns
- Modular widget creation
- Proper event binding and callback management

## 🏗️ Project Structure

```
Calculator/
├─ .github/                # GitHub metadata (workflows/templates)
├─ .gitignore              # Files/dirs ignored by git
├─ Kivy-APK-AAB.md         # Detailed guide: building APK to AAB with Kivy/Buildozer
├─ README.md               # Descriptions about the project
├─ assets/                 # Static assets (icons, screenshots, images)
├─ buildozer.spec          # Buildozer config for packaging to Android/iOS
├─ main.py                 # Kivy/KivyMD app runtime
└─ requirements.txt        # Python dependencies
```

## 📋 Requirements

- Python 3.x
- Kivy 2.3.1
- Buildozer (for mobile deployment)

## 🚦 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anas436/Calculator.git
   cd Calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Build for mobile (Android)**
   ```bash
   buildozer android debug
   ```

## 🎯 Skills Demonstrated

- **Mobile App Development**: Cross-platform application creation
- **UI/UX Design**: Intuitive user interface implementation
- **Python Programming**: Object-oriented design and event handling
- **Kivy Framework**: Mastery of widgets, layouts, and properties
- **Problem Solving**: Input validation and error prevention
- **Software Architecture**: Clean, maintainable code structure
- **Build & Deployment**: Mobile app packaging and distribution

## 🔄 Future Enhancements

- Scientific calculator functions
- Calculation history
- Theme customization
- Voice input support
- Cloud synchronization

---
*Ready to bring this level of quality and attention to detail to your development team!*
