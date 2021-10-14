class GroupBy:
    def __init__(self, group: str = "author",
                 layout: str = "Created by {author}\n{__layout__}") -> None:
        """Group requirements

        Parameters
        ----------
        group : str, optional
            The Pypi info parameter to group by.
            by default "author"
        layout : str, optional
            The layout of the groupping, any Pypi info parameter
            use '__layout__' to insert layout string,
            by default "Created by {author}\n{__layout__}"
        """

        self._group = group
        self._layout = layout

    @property
    def group(self) -> str:
        return self._group

    @property
    def layout(self) -> str:
        return self._layout
