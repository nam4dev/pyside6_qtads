import platform
# Auto generated file

if platform.system() == 'Windows':
	import os
	import PySide6
	import shiboken6

	def load_dll(path):
		return os.add_dll_directory(os.path.dirname(path))

	with load_dll(PySide6.__file__), load_dll(shiboken6.__file__):
		from .PySide6QtAds import ads
else:
	# Runtime library dependencies resolved via rpath
	from .PySide6QtAds import ads


TabInvalidIndex = ads.eTabIndex.TabInvalidIndex
TabDefaultInsertIndex = ads.eTabIndex.TabDefaultInsertIndex

# DockWidgetArea
DockWidgetArea = ads.DockWidgetArea
NoDockWidgetArea = ads.NoDockWidgetArea
LeftDockWidgetArea = ads.LeftDockWidgetArea
RightDockWidgetArea = ads.RightDockWidgetArea
TopDockWidgetArea = ads.TopDockWidgetArea
BottomDockWidgetArea = ads.BottomDockWidgetArea
CenterDockWidgetArea = ads.CenterDockWidgetArea
InvalidDockWidgetArea = ads.InvalidDockWidgetArea
OuterDockAreas = ads.OuterDockAreas
AllDockAreas = ads.AllDockAreas

# eBitwiseOperator
BitwiseAnd = ads.BitwiseAnd
BitwiseOr = ads.BitwiseOr

# eDragState
DraggingInactive = ads.DraggingInactive
DraggingMousePressed = ads.DraggingMousePressed
DraggingTab = ads.DraggingTab
DraggingFloatingWidget = ads.DraggingFloatingWidget

# eIcon
TabCloseIcon = ads.TabCloseIcon
DockAreaMenuIcon = ads.DockAreaMenuIcon
DockAreaUndockIcon = ads.DockAreaUndockIcon
DockAreaCloseIcon = ads.DockAreaCloseIcon
IconCount = ads.IconCount

# TitleBarButton
TitleBarButtonTabsMenu = ads.TitleBarButtonTabsMenu
TitleBarButtonUndock = ads.TitleBarButtonUndock
TitleBarButtonClose = ads.TitleBarButtonClose

# Classes
CDockAreaTabBar = ads.CDockAreaTabBar
CDockAreaTitleBar = ads.CDockAreaTitleBar
CDockAreaWidget = ads.CDockAreaWidget
CDockComponentsFactory = ads.CDockComponentsFactory
CDockContainerWidget = ads.CDockContainerWidget
CDockFocusController = ads.CDockFocusController
CDockManager = ads.CDockManager
CDockSplitter = ads.CDockSplitter
CDockOverlay = ads.CDockOverlay
CDockOverlayCross = ads.CDockOverlayCross
CDockWidget = ads.CDockWidget
CDockWidgetTab = ads.CDockWidgetTab
CDockingStateReader = ads.CDockingStateReader
CElidingLabel = ads.CElidingLabel
CFloatingDockContainer = ads.CFloatingDockContainer
CFloatingDragPreview = ads.CFloatingDragPreview
IFloatingWidget = ads.IFloatingWidget
CIconProvider = ads.CIconProvider
CSpacerWidget = ads.CSpacerWidget
CTitleBarButton = ads.CTitleBarButton

# Auto-hide related
CAutoHideTab = ads.CAutoHideTab
CAutoHideSideBar = ads.CAutoHideSideBar
CAutoHideDockContainer = ads.CAutoHideDockContainer

# SideBarLocation
SideBarLocation = ads.SideBarLocation
