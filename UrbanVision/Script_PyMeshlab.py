import pymeshlab
import os.path,subprocess
from subprocess import STDOUT,PIPE

inputName = "meshed-poisson"
internName = inputName+"_Clean"
outputName = inputName

ms = pymeshlab.MeshSet()
ms.load_new_mesh('ply/'+inputName+'.ply')

ms.remove_isolated_pieces_wrt_diameter(mincomponentdiag = 3, removeunref = True)
ms.merge_close_vertices()

ms.save_current_mesh(file_name = 'ply/'+ internName+'.ply', 
                     binary = False,
                     save_vertex_quality = False,
                     save_vertex_flag = False,
                     save_vertex_color = True,
                     save_vertex_coord = True,
                     save_vertex_normal = True,
                     save_vertex_radius = False,
                     save_face_quality = False,
                     save_face_flag = False,
                     save_face_color = False,
                     save_wedge_color = False,
                     save_wedge_texcoord = False,
                     save_wedge_normal = False,
                     save_polygonal = False)
                     
cmd = ['java', 'Main','ply/'+internName+'.ply',outputName]
proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
