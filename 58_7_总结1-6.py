__author__ = 'Hk4Fun'
__date__ = '2018/2/28 16:12'

'''对58_1至58_6的简单总结：

             中序遍历               前序遍历                             后序遍历

上一个结点   有右找右的最左；        有左则为该左；                       为其父的右且其父有左，
             无右则向上找第一个      无左有右则为该右；                   则为其父左子树的最右叶结点；
             为其父的左的父          无左无右则为第一个                   其他情况下
                                    右兄弟或右堂兄弟                      为其父的右且其父无左或为其父的左）为其父

下一个结点   有左找左的最右；        为其父的右且其父有左，                有左则为该左；
             无左则向上找第一个      则为其父左子树的最右叶结点；          无左有右则为该右；
             为其父的右的父          其他情况下                           无左无右则为第一个
                                   （为其父的右且其父无左或为其父的左）    右兄弟或右堂兄弟
                                    为其父
对比发现：                                    
寻找中序遍历上一个结点和下一个结点的方法是对称的，
而寻找前序遍历上一个结点和后序遍历下一个结点的方法是对称的，
寻找前序遍历下一个结点和后序遍历上一个结点的方法是对称的，
'''
