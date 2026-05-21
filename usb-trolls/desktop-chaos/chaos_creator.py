#!/usr/bin/env python3
"""
Desktop Chaos Creator Troll
Fills the desktop with random, harmless files when USB is plugged in
"""

import os
import random
from pathlib import Path
from datetime import datetime

class DesktopChaosTroll:
    def __init__(self):
        self.file_templates = {
            "text": [
                "This is not a virus.txt",
                "Check_Your_Downloads.txt",
                "You_Got_Trolled.txt",
                "Read_Me_I_Guess.txt",
                "Definitely_Not_Important.txt",
            ],
            "shortcuts": [
                "Open_Me.webloc",
                "Important_Update.webloc",
                "Your_System_Has_Warnings.webloc",
            ],
            "folders": [
                "❌_Error_Report",
                "🔴_Critical_Alert",
                "💾_Recovery_Files",
                "⚠️_System_Backup",
                "🚨_Emergency_Files",
            ]
        }
        
        self.file_contents = {
            "This is not a virus.txt": "👋 Hello! I'm definitely not a virus.\nI'm just a friendly USB drive pranking you!\nHave a nice day! 😄",
            "You_Got_Trolled.txt": "CONGRATULATIONS!\n\nYou've been successfully trolled!\n\nYour computer is fine. Really!\nThis was all just a harmless prank.\n\n🎉 Well played, USB drive. Well played.",
            "Definitely_Not_Important.txt": "This file is definitely not important.\nPlease do not delete it.\nJK lol delete it if you want 🤪",
        }
    
    def create_fake_link(self, filename, url):
        """Create a .webloc file (macOS web link)"""
        webloc_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>URL</key>
    <string>{url}</string>
</dict>
</plist>'''
        return webloc_content
    
    def create_chaos_files(self, desktop_path):
        """Create random chaos files on desktop"""
        desktop = Path(desktop_path)
        
        if not desktop.exists():
            print(f"❌ Desktop path not found: {desktop_path}")
            return
        
        print(f"📄 Creating chaos files on {desktop}")
        print("-" * 50)
        
        files_created = 0
        
        # Create random text files
        num_text = random.randint(3, 8)
        for i in range(num_text):
            filename = random.choice(self.file_templates["text"])
            filepath = desktop / filename
            
            content = self.file_contents.get(
                filename,
                f"File #{i+1}\nCreated by Desktop Chaos Troll\nTime: {datetime.now()}"
            )
            
            filepath.write_text(content)
            print(f"  ✓ Created {filename}")
            files_created += 1
        
        # Create random folders
        num_folders = random.randint(1, 3)
        for i in range(num_folders):
            foldername = random.choice(self.file_templates["folders"])
            folderpath = desktop / foldername
            folderpath.mkdir(exist_ok=True)
            
            # Add a file inside
            readme = folderpath / "README.txt"
            readme.write_text("This folder was created by a USB troll. Nothing to see here! 😄")
            
            print(f"  ✓ Created folder {foldername}/")
            files_created += 1
        
        # Create web shortcuts
        webloc_urls = {
            "You_Should_Check_This.webloc": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "Definitely_Click_Me.webloc": "https://en.wikipedia.org/wiki/Trollface",
        }
        
        for filename, url in webloc_urls.items():
            filepath = desktop / filename
            content = self.create_fake_link(filename, url)
            filepath.write_text(content)
            print(f"  ✓ Created shortcut {filename}")
            files_created += 1
        
        print()
        print(f"✅ Chaos created! ({files_created} files/folders)")
        return files_created
    
    def create_launch_script(self, usb_path):
        """Create a script to auto-run on USB mount"""
        script = f'''#!/bin/bash
# Auto-run chaos on USB mount

DESKTOP="$HOME/Desktop"
FILES_CREATED=0

# Create files
for i in {{1..{random.randint(3, 8)}}}; do
    touch "$DESKTOP/chaos_file_$i.txt"
    echo "Chaos!" > "$DESKTOP/chaos_file_$i.txt"
    ((FILES_CREATED++))
done

# Show notification
osascript -e 'display notification "Desktop chaos initiated!" with title "USB Troll"'

echo "$FILES_CREATED files created on desktop!"
'''
        return script
    
    def install(self, desktop_path=None):
        """Install the desktop chaos troll"""
        print("=" * 50)
        print("🌪️  DESKTOP CHAOS CREATOR TROLL 🌪️")
        print("=" * 50)
        print()
        
        if desktop_path is None:
            desktop_path = os.path.expanduser("~/Desktop")
        
        files_created = self.create_chaos_files(desktop_path)
        
        print()
        print("💡 Prank completed!")
        print(f"   Your victim will find {files_created} mysterious files on their desktop!")
        print()
        print("🎨 Files are harmless and easily deleted.")
        print("   Watch as they get confused! 😄")

if __name__ == "__main__":
    import sys
    
    desktop = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Desktop")
    chaos = DesktopChaosTroll()
    chaos.install(desktop)
