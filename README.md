# Instructions for Docker Container

1. Build \
   From folder containing Docker file \
   `docker build -t nle-container .` \
   Will take a few gigs of disk space tho. \
   Will name image nle-container.
2. Run \
   `docker run -it nle-container` \
3. Run program: \
   From container testProg: `python rando1000.py` \
4. Play as human: \
   `python -m nle.scripts.play --env NetHackChallenge-v0`
5. I used Remote - Containers extenstion in Visual Studio Code \
   to open and edit the `main.py` from inside of the terminal. \
   In VSCode, `CRTL-Shift-p`, type `Remote-Containers: Open Folder in Container...`
