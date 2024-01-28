# Desafio 021: Faça um programa em Python que abra e reproduza um áudio de um arquivo mp3.
# -*- encoding: utf-8 -*-

import pygame

pygame.init()

pygame.mixer.music.load("ex.021musica.mp3")

pygame.mixer.music.play()

input()

pygame.event.wait()

# Música: Dreamscape por: 009 SoundSystem
# Sim, aquela música de tutorial de youtube véia pra cacete kkkk
