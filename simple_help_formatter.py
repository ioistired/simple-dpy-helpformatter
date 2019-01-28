# encoding: utf-8

# MIT License
#
# Copyright © 2019 Benjamin Mintz <bmintz@protonmail.com>
# Copyright © 2015-2017 Rapptz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import inspect
import itertools

from discord.ext import commands

class HelpFormatter(commands.HelpFormatter):
	def get_command_signature(self):
		return '`' + super().get_command_signature() + '`'

	def get_ending_note(self):
		command_name = self.context.invoked_with
		return (
			"Type `{0}{1}` command for more info on a command.\n"
			"You can also type `{0}{1} category` for more info on a category.".format(self.clean_prefix, command_name))

	def _add_subcommands_to_page(self, max_width, commands):
		for name, command in commands:
			if name in command.aliases:
				# skip aliases
				continue

			self._paginator.add_line(f'**{name}**')
			self._paginator.add_line(command.short_doc)

	async def format(self):
		"""Handles the actual behaviour involved with formatting.

		Returns
		--------
		list
			A paginated output of the help command.
		"""
		self._paginator = commands.Paginator(prefix='', suffix='')

		description = self.command.description if not self.is_cog() else inspect.getdoc(self.command)

		if description:
			# <description> portion
			self._paginator.add_line(description, empty=True)

		if isinstance(self.command, commands.Command):
			# <signature portion>
			signature = self.get_command_signature()
			self._paginator.add_line(signature, empty=True)

			# <long doc> section
			if self.command.help:
				self._paginator.add_line(self.command.help, empty=True)

			# end it here if it's just a regular command
			if not self.has_subcommands():
				self._paginator.close_page()
				return self._paginator.pages

		max_width = self.max_name_size

		def category(tup):
			cog = tup[1].cog_name
			# we insert the zero width space there to give it approximate
			# last place sorting position.
			return f'***{cog}:***' if cog is not None else '\u200b***No Category:***'

		filtered = await self.filter_command_list()
		if self.is_bot():
			data = sorted(filtered, key=category)
			for category, category_commands in itertools.groupby(data, key=category):
				# there simply is no prettier way of doing this.
				category_commands = sorted(category_commands)
				if len(category_commands) > 0:
					self._paginator.add_line(category)

				self._add_subcommands_to_page(max_width, category_commands)
		else:
			filtered = sorted(filtered)
			if filtered:
				self._paginator.add_line('Commands:')
				self._add_subcommands_to_page(max_width, filtered)

		# add the ending note
		self._paginator.add_line()
		ending_note = self.get_ending_note()
		self._paginator.add_line(ending_note)
		return self._paginator.pages
