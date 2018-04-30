import maya.cmds as cmds

class ARKIT2MAYA:
    '''
    frame data format:
    total:      1273
    0:          cm
    1:          fm
    2~1221:     v
    1222~1272:  blendshape
    '''
    
    def __init__(self):
        window = cmds.window( width = 550 ,title= "ARKIT2MAYA",height = 800)
        cmds.rowLayout("rl",numberOfColumns=2, columnWidth2=(150, 400,), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'left', 0), (2, 'left', 0)] )
        
        cmds.columnLayout(columnWidth=100, rowSpacing=20,parent = "rl")
        
        cmds.rowLayout(numberOfColumns=2)
        cmds.text( label='CFrame',width = 50 )
        cmds.textField("frame_index",text = "0",width = 90)
        
        cmds.setParent( '..' )
        cmds.button( label = "load Data", command = self.load_data)        
        cmds.button( label = "get frame count", command = self.get_frame_count)
        cmds.button( label = "get current frame", command = self.get_current_frame)

        cmds.button( label = "apply transform", command = self.apply_transform)
        cmds.button( label = "apply vertex", command = self.apply_vertex)
        cmds.button( label = "apply blendshape",command = self.apply_blendshape)
        cmds.button( label = "info",command = self.info)
        
        cmds.columnLayout(columnWidth=400,parent = "rl" )
        cmds.scrollField("sf",editable=False, wordWrap=True, text='''
        
    ::VRKIT2MAYA::
    author: horsetery chen
    data: 20180425
    -----------------------
    face data:
        frame data format:
        total:      1273
        0:          cm
        1:          fm
        2~1221:     vertex
        1222~1272:  blendshape
        
    data interface:
        vertice:             self.vertexes
        cameraTransform:     self.cm
        faceTransform:       self.fm
        blendshape:          self.blendshape
        ''',height = 800,width = 400)
        cmds.showWindow(window)
        self.data = []
        self.current_frame_data=[0]
        self.cm = []
        self.fm = []
        self.vertexes = []
        self.blendshapes =[]
    def get_frame_count(self,*args):
        cmds.scrollField("sf",edit = True,text = len(self.data))
    def get_current_frame(self,*args):
        try:
            index = int(cmds.textField("frame_index",query = True,text = True ))
            self.current_frame_data = self.data[index].split('~')
            cmds.scrollField("sf",edit = True,text ='''current frame data load...\n
            frame index :%s\n
            data length: %s
            '''%(index,len(self.current_frame_data)))
        except:
            cmds.scrollField("sf",edit = True,text ="Can't load current frame data£¡")
        
    def load_data(self,*args):
        basicFilter = "*.txt"
        try:
            path = cmds.fileDialog2(fileMode=1,fileFilter=basicFilter, dialogStyle=2)[0]
            self.data = open(path).readlines()
            cmds.scrollField("sf",edit = True,text ="data loaded!")
        except:
            cmds.scrollField("sf",edit = True,text ="Please load the correct file£¡")
        print("load_data")
        
    def apply_transform(self,*args):
        cm_str = "cm: "
        fm_str = "fm: "        
        cm_data = self.current_frame_data[0].split(":")
        fm_data = self.current_frame_data[1].split(":")        
        self.cm = cm_data
        self.fm = fm_data
        for i in cm_data:
            cm_str = "%s\n%s"%(cm_str,i)
        for i in fm_data:
            fm_str = "%s\n%s"%(fm_str,i)    
        
        cmds.scrollField("sf",edit = True,text = "%s\n%s"%(cm_str,fm_str))
        print("transform")
        
    def get_pre(self,a):
        print(a[0])
        print(a[1])
        print(a[2])
        return get_pre(a[3:])
        
    def apply_vertex(self,*args):
        vertexes = self.current_frame_data[2:1222]
        
        for i,v in enumerate(vertexes):
            v_=[]
            for j,vv in enumerate(v.split(":")):
                v_.append(float(vv))
            self.vertexes.append(v_)
        vs=""
        for i,v in enumerate(self.vertexes):
            vs = "%s\n index%s: x: %s,y: %s,z: %s"%(vs,i,v[0],v[1],v[2])
        cmds.scrollField("sf",edit = True,text =vs)
        print("vertex")
        
    def apply_blendshape(self,*args):
        bs = ""
        blendshapes = self.current_frame_data[1222:1273]
        for i,v in enumerate(blendshapes):
            self.blendshapes.append(v)
            bs = "%s\n%s"%(bs,v)
        cmds.scrollField("sf",edit = True,text =bs)
        print("blendshape")
        
    def info(self,*args):
        info ='''
    ::VRKIT2MAYA::
    author: horsetery chen
    data: 20180425
    -----------------------
    face data:
        frame data format:
        total:      1273
        0:          cm
        1:          fm
        2~1221:     vertex
        1222~1272:  blendshape
        
    data interface:
        vertice:             self.vertexes
        cameraTransform:     self.cm
        faceTransform:       self.fm
        blendshape:          self.blendshape
        '''
        cmds.scrollField("sf",edit = True,text =info)
        
am = ARKIT2MAYA()
