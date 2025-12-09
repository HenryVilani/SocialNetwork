from abc import ABC
from typing import Optional

from src.application.dtos.channel_repo_dto import CreateChannelRepoInDTO, SegmentChannelRepoOutDTO, UpdateChannelRepoInDTO
from src.domain.entities.channel_entity import Channel


class IChannelRepository(ABC):
    """
    Repository interface for channel persistence operations.
    """

    def create(self, channel: CreateChannelRepoInDTO) -> Channel:
        """
        Create a new channel.

        :param channel: Input data for channel creation.
        :type channel: CreateChannelRepoInDTO
        :return: Created channel entity.
        :rtype: Channel
        """
        ...

    def update(self, channel_id: str, channel: UpdateChannelRepoInDTO) -> Channel:
        """
        Update an existing channel.

        :param channel_id: Id of the channel to update.
        :type channel_id: str
        :param channel: Input data to update channel.
        :type channel: UpdateChannelRepoInDTO
        :return: Updated channel entity.
        :rtype: Channel
        """
        ...

    def delete(self, channel_id: str) -> None:
        """
        Delete a channel by id.

        :param channel_id: Id of the channel to delete.
        :type channel_id: str
        :rtype: None
        """
        ...

    def delete_all_by_user(self, user_id: str) -> None:
        """
        Delete all channels associated with a specific user.

        :param user_id: Id of the user whose channels must be deleted.
        :type user_id: str
        :rtype: None
        """
        ...

    def find_by_id(self, channel_id: str) -> Optional[Channel]:
        """
        Retrieve a channel by id.

        :param channel_id: Id of the channel to retrieve.
        :type channel_id: str
        :return: Channel entity if found; otherwise None.
        :rtype: Optional[Channel]
        """
        ...

    def find_all_by_name(self, name: str, length: int, segment: int) -> SegmentChannelRepoOutDTO:
        """
        Retrieve channels filtered by name with pagination support.

        :param name: Name filter for the query.
        :type name: str
        :param length: Maximum number of items to return.
        :type length: int
        :param segment: Pagination segment (offset).
        :type segment: int
        :return: Result set containing channels and pagination metadata.
        :rtype: SegmentChannelRepoOutDTO
        """
        ...
